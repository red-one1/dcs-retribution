from __future__ import annotations

import base64
import collections
import json
import io
import logging
import pickle
import shutil
import typing
import types
from pathlib import Path
from typing import Optional, TYPE_CHECKING, Any

import dcs.terrain.falklands.airports
from dcs.terrain.terrain import Terrain

import pydcs_extensions
import jsonpickle
from jsonpickle import (
    handlers,
    tags,
    pickler as jsonpickle_pickler,
    unpickler as jsonpickle_unpickler,
)
from game.profiling import logged_duration
from game.dcs.shipunittype import ShipUnitType
from pydcs_extensions import (
    ELM2084_MMR_AD_RT,
    Iron_Dome_David_Sling_CP,
    RBS_70,
    RBS_90,
    CH_BVS10,
    Artillerisystem08_M982,
)

if TYPE_CHECKING:
    from game import Game

_dcs_saved_game_folder: Optional[str] = None
_prefer_liberation_payloads: bool = False
_server_port: int = 16880
_save_format: str = "classic"

SAVE_FORMAT_CLASSIC = "classic"
SAVE_FORMAT_PLAIN_TEXT = "plain_text"


class _TypingAliasHandler(handlers.BaseHandler):
    def flatten(self, obj: Any, data: dict[str, Any]) -> Any:
        return str(obj)


class _DefaultDictHandler(handlers.BaseHandler):
    def flatten(self, obj: collections.defaultdict, data: dict[str, Any]) -> Any:
        factory = obj.default_factory
        factory_repr = None if factory is None else repr(factory)
        return {
            "default_factory": factory_repr,
            "items": self.context.flatten(dict(obj), reset=False),
        }

    def restore(self, obj: dict[str, Any]) -> collections.defaultdict:
        factory_repr = obj.get("default_factory")
        if factory_repr in {"typing.Set", "set", "builtins.set", "<class 'set'>"}:
            factory = set
        else:
            factory = None
        items = self.context.restore(obj.get("items", {}), reset=False)
        return collections.defaultdict(factory, items)


class _ShipUnitTypeHandler(handlers.BaseHandler):
    def flatten(self, obj: ShipUnitType, data: dict[str, Any]) -> Any:
        data[tags.OBJECT] = f"{ShipUnitType.__module__}.ShipUnitType"
        data["variant_id"] = obj.variant_id
        return data

    def restore(self, obj: dict[str, Any]) -> ShipUnitType:
        return ShipUnitType.named(obj["variant_id"])


class _TerrainHandler(handlers.BaseHandler):
    def flatten(self, obj: Terrain, data: dict[str, Any]) -> Any:
        payload = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
        data["payload"] = base64.b64encode(payload).decode("ascii")
        return data

    def restore(self, obj: dict[str, Any]) -> Terrain:
        payload = base64.b64decode(obj["payload"])
        return pickle.loads(payload)


def _register_jsonpickle_handlers() -> None:
    handlers.register(collections.defaultdict, _DefaultDictHandler, base=True)
    handlers.register(ShipUnitType, _ShipUnitTypeHandler)
    handlers.register(Terrain, _TerrainHandler, base=True)
    for alias_type in (
        getattr(typing, "_GenericAlias", None),
        getattr(typing, "_SpecialGenericAlias", None),
        getattr(typing, "_CallableGenericAlias", None),
        getattr(typing, "ForwardRef", None),
        getattr(typing, "TypeVar", None),
        getattr(typing, "ParamSpec", None),
        getattr(typing, "TypeVarTuple", None),
    ):
        if alias_type is not None:
            handlers.register(alias_type, _TypingAliasHandler)
    union_type = getattr(types, "UnionType", None)
    if union_type is not None:
        handlers.register(union_type, _TypingAliasHandler)
    for alias in (
        getattr(typing, "Set", None),
        getattr(typing, "List", None),
        getattr(typing, "Dict", None),
        getattr(typing, "Tuple", None),
        getattr(typing, "FrozenSet", None),
        getattr(typing, "Optional", None),
        getattr(typing, "Union", None),
    ):
        if alias is not None and isinstance(alias, type):
            handlers.register(alias, _TypingAliasHandler)


_JSON_MIGRATION_MAP: dict[str, str] = {
    "pydcs_extensions.f4b.f4b.": "pydcs_extensions.f4.f4.",
    "pydcs_extensions.irondome.irondome.ELM2048_MMR": "pydcs_extensions.irondome.irondome.ELM2084_MMR_AD_RT",
    "pydcs_extensions.irondome.irondome.IRON_DOME_CP": "pydcs_extensions.irondome.irondome.Iron_Dome_David_Sling_CP",
    "pydcs_extensions.swedishmilitaryassetspack.swedishmilitaryassetspack.BV410_RBS90": "pydcs_extensions.swedishmilitaryassetspack.swedishmilitaryassetspack.RBS_90",
    "pydcs_extensions.swedishmilitaryassetspack.swedishmilitaryassetspack.BV410": "pydcs_extensions.swedishmilitaryassetspack.swedishmilitaryassetspack.CH_BVS10",
    "pydcs_extensions.swedishmilitaryassetspack.swedishmilitaryassetspack.Artillerisystem08": "pydcs_extensions.swedishmilitaryassetspack.swedishmilitaryassetspack.Artillerisystem08_M982",
    "pydcs_extensions.swedishmilitaryassetspack.swedishmilitaryassetspack.BV410_RBS70": "pydcs_extensions.swedishmilitaryassetspack.swedishmilitaryassetspack.RBS_70",
    "pydcs_extensions.fa18efg.Superbug_AITanker": "pydcs_extensions.fa18efg.FA_18ET",
    "pydcs_extensions.su30.Su_30MKA_AG": "pydcs_extensions.su30.Su_30MKA",
    "pydcs_extensions.su30.Su_30MKI_AG": "pydcs_extensions.su30.Su_30MKI",
    "pydcs_extensions.su30.Su_30SM_AG": "pydcs_extensions.su30.Su_30SM",
    "pydcs_extensions.su30.Su_30MKM_AG": "pydcs_extensions.su30.Su_30MKM",
    "pydcs_extensions.SaveManager": "game.persistency.DummyObject",
    "pydcs_extensions.SaveGameBundle": "game.persistency.DummyObject",
    "dcs.terrain.falklands.airports.CaletaTortel": "dcs.terrain.Airport",
    "dcs.terrain.falklands.airports.Caleta_Tortel_Airport": "dcs.terrain.Airport",
}


def _apply_json_migration_map(raw_text: str) -> str:
    for old, new in _JSON_MIGRATION_MAP.items():
        raw_text = raw_text.replace(old, new)
    return raw_text


def _coerce_unhashable_sets(value: Any) -> Any:
    if isinstance(value, list):
        return [_coerce_unhashable_sets(item) for item in value]
    if isinstance(value, dict):
        if tags.SET in value and isinstance(value[tags.SET], list):
            items = [_coerce_unhashable_sets(item) for item in value[tags.SET]]
            if any(isinstance(item, (dict, list)) for item in items):
                return {tags.TUPLE: items}
            return {tags.SET: items}
        return {key: _coerce_unhashable_sets(val) for key, val in value.items()}
    return value


# fmt: off
class DummyObject:
    def __setstate__(self, state: dict[str, Any]) -> None:
        self.__dict__.update(state)


class MigrationUnpickler(pickle.Unpickler):
    """Custom unpickler to migrate campaign save-files for when components have been moved"""

    def find_class(self, module: Any, name: str) -> Any:
        handlers = [
            self._handle_airport_migrations,
            self._handle_weather_classes,
            self._handle_ch_russian_assets,
            self._handle_su30,
            self._handle_misc,
        ]

        for handler in handlers:
            result = handler(module, name)
            if result is not None:
                return result

        # Fallback to default behavior with special handling
        return self._handle_default(module, name)

    def _handle_airport_migrations(self, module: str, name: str) -> Any:
        """Handle airport name changes across all terrains"""
        # Kola terrain airports
        if module == "dcs.terrain.kola.airports":
            if name == "Lakselv":
                from dcs.terrain.kola.airports import Banak
                return Banak
            elif name == "Severomorsk1":
                from dcs.terrain.kola.airports import Severomorsk_1
                return Severomorsk_1
            elif name == "Severomorsk3":
                from dcs.terrain.kola.airports import Severomorsk_3
                return Severomorsk_3
            elif name == "Olenegorsk":
                from dcs.terrain.kola.airports import Olenya
                return Olenya
            elif name == "Bas_100":
                from dcs.terrain.kola.airports import Vuojarvi
                return Vuojarvi
            elif name == "Alakourtti":
                from dcs.terrain.kola.airports import Alakurtti
                return Alakurtti
        
        # Sinai terrain airports
        if module == "dcs.terrain.sinai.airports":
            if name == "Borj_El_Arab_International_Airport":
                from dcs.terrain.sinai.airports import Borg_El_Arab_International_Airport
                return Borg_El_Arab_International_Airport
            elif name == "Palmahim":
                from dcs.terrain.sinai.airports import Palmachim
                return Palmachim
        
        # Syria terrain airports
        if module == "dcs.terrain.syria.airports":
            if name == "Amman":
                from dcs.terrain.syria.airports import Marka
                return Marka
            elif name in ["Helipad_88", "Helipad_183", "Helipad_217", "Helipad_218"]:
                return dcs.terrain.Airport  # use base-class if airport was removed
        
        # Afghanistan terrain airports
        if module == "dcs.terrain.afghanistan.airports":
            if name == "Khost_Heliport":
                from dcs.terrain.afghanistan.airports import FOB_Salerno
                return FOB_Salerno
        
        # Falklands terrain airports
        if module == "dcs.terrain.falklands.airports":
            if name == "Aerodromo_De_Tolhuin":
                from dcs.terrain.falklands.airports import Tolhuin
                return Tolhuin
            elif name == "Porvenir_Airfield":
                from dcs.terrain.falklands.airports import Porvenir
                return Porvenir
            elif name == "Aeropuerto_de_Gobernador_Gregores":
                from dcs.terrain.falklands.airports import Gobernador_Gregores
                return Gobernador_Gregores
            elif name == "Aerodromo_O_Higgins":
                from dcs.terrain.falklands.airports import O_Higgins
                return O_Higgins
            elif name == "Hipico":
                from dcs.terrain.falklands.airports import Hipico_Flying_Club
                return Hipico_Flying_Club
        
        # Germany Cold War terrain airports
        if module == "dcs.terrain.germanycoldwar.airports":
            if name == "Leipzig_Halle":
                from dcs.terrain.germanycoldwar.airports import Schkeuditz
                return Schkeuditz
        
        return None

    def _handle_weather_classes(self, module: str, name: str) -> Any:
        """Handle migrations for weather-related classes"""
        if name == "NightMissions":
            from game.settings import NightMissions
            return NightMissions
        if name == "Conditions":
            from game.weather.conditions import Conditions
            return Conditions
        if name == "AtmosphericConditions":
            from game.weather.atmosphericconditions import AtmosphericConditions
            return AtmosphericConditions
        if name == "WindConditions":
            from game.weather.wind import WindConditions
            return WindConditions
        if name == "Clouds":
            from game.weather.clouds import Clouds
            return Clouds
        if name == "Fog":
            from game.weather.fog import Fog
            return Fog
        if name == "ClearSkies":
            from game.weather.weather import ClearSkies
            return ClearSkies
        if name == "Cloudy":
            from game.weather.weather import Cloudy
            return Cloudy
        if name == "Raining":
            from game.weather.weather import Raining
            return Raining
        if name == "Thunderstorm":
            from game.weather.weather import Thunderstorm
            return Thunderstorm
        
        return None

    def _handle_ch_russian_assets(self, module: str, name: str) -> Any:
        """Handle migrations for Russian military assets pack"""
        if module != "pydcs_extensions.russianmilitaryassetspack.russianmilitaryassetspack":
            return None
        
        if name == "Admiral_Gorshkov":
            from pydcs_extensions.russianmilitaryassetspack import CH_Admiral_Gorshkov
            return CH_Admiral_Gorshkov
        if name == "Karakurt_AShM":
            from pydcs_extensions.russianmilitaryassetspack import CH_Karakurt_AShM
            return CH_Karakurt_AShM
        if name == "Karakurt_LACM":
            from pydcs_extensions.russianmilitaryassetspack import CH_Karakurt_LACM
            return CH_Karakurt_LACM
        if name == "K300P":
            from pydcs_extensions.russianmilitaryassetspack import CH_K300P
            return CH_K300P
        if name == "MonolitB":
            from pydcs_extensions.russianmilitaryassetspack import CH_MonolitB
            return CH_MonolitB
        if name == "TorM2K":
            from pydcs_extensions.russianmilitaryassetspack import CH_TorM2K
            return CH_TorM2K
        if name == "PantsirS2":
            from pydcs_extensions.russianmilitaryassetspack import CH_PantsirS2
            return CH_PantsirS2
        if name == "CH_TOS1A":
            from dcs.vehicles import Artillery
            return Artillery.CHAP_TOS1A
        if name == "CH_Mi28N":
            from dcs.helicopters import Mi_28N
            return Mi_28N
        if name == "CH_Tu_95MSM":
            from dcs.planes import Tu_95MS
            return Tu_95MS
        if name == "PantsirS1":
            from dcs.vehicles import AirDefence
            return AirDefence.CHAP_PantsirS1
        if name == "TorM2":
            from dcs.vehicles import AirDefence
            return AirDefence.CHAP_TorM2
        if name == "TorM2M":
            from dcs.vehicles import AirDefence
            return AirDefence.CHAP_TorM2
        if name == "CH_T90A":
            from dcs.vehicles import Armor
            return Armor.CHAP_T90M
        if name == "CH_T90M":
            from dcs.vehicles import Armor
            return Armor.CHAP_T90M
        if name == "CH_IskanderM":
            from dcs.vehicles import MissilesSS
            return MissilesSS.CHAP_9K720_HE
        if name == "CH_Project22160":
            from dcs.ships import CHAP_Project22160
            return CHAP_Project22160
        
        return None
    
    def _handle_su30(self, module: str, name: str) -> Any:
        """Handle migrations for Su-30 aircraft variants"""
        if name == "Su_30MKA_AG":
            from pydcs_extensions.su30 import Su_30MKA
            return Su_30MKA
        if name == "Su_30MKI_AG":
            from pydcs_extensions.su30 import Su_30MKI
            return Su_30MKI
        if name == "Su_30SM_AG":
            from pydcs_extensions.su30 import Su_30SM
            return Su_30SM
        if name == "Su_30MKM_AG":
            from pydcs_extensions.su30 import Su_30MKM
            return Su_30MKM

        return None
    
    def _handle_misc(self, module: str, name: str) -> Any:
        """Handle migrations for mods"""
        if module == "pydcs_extensions.f4b.f4b":
            return pydcs_extensions.f4

        if module == "pydcs_extensions.irondome.irondome":
            if name in ["I9K57_URAGAN", "I9K51_GRAD", "I9K58_SMERCH"]:
                return None
            elif name == "ELM2048_MMR":
                return ELM2084_MMR_AD_RT
            elif name == "IRON_DOME_CP":
                return Iron_Dome_David_Sling_CP
        
        if module == "pydcs_extensions.swedishmilitaryassetspack.swedishmilitaryassetspack":
            if name == "BV410_RBS90":
                return RBS_90
            elif name == "BV410":
                return CH_BVS10
            elif name == "Artillerisystem08":
                return Artillerisystem08_M982
            elif name == "BV410_RBS70":
                return RBS_70
        
        if name == "Superbug_AITanker":
            return pydcs_extensions.fa18efg.FA_18ET
        
        if name in ["SaveManager", "SaveGameBundle"]:
            return DummyObject
        if name in ["CaletaTortel", "Caleta_Tortel_Airport"]:
            return dcs.terrain.Airport  # use base-class if airport was removed
        
        return None
    
    def _handle_default(self, module: str, name: str) -> Any:
        """Handle default class resolution with fallback logic"""
        # Special handling for vehicles and ships with case conversion
        if module in ["dcs.vehicles", "dcs.ships"]:
            try:
                return super().find_class(module, name)
            except AttributeError:
                alternate = name.split('.')[:-1] + [name.split('.')[-1][0].lower() + name.split('.')[-1][1:]]
                name = '.'.join(alternate)
        try:
            return super().find_class(module, name)
        except AttributeError:
            if "dcs.terrain" in module and "airports" not in module:
                module = f"{module}.airports"
            else:
                raise
        return super().find_class(module, name)
# fmt: on


def _create_dir_if_needed(path: Path) -> Path:
    if not path.exists():
        path.mkdir(755, parents=True)
    return path


def setup(
    user_folder: str,
    prefer_liberation_payloads: bool,
    port: int,
    save_format: str = SAVE_FORMAT_CLASSIC,
) -> None:
    global _dcs_saved_game_folder
    global _prefer_liberation_payloads
    global _server_port
    global _save_format
    _dcs_saved_game_folder = user_folder
    _prefer_liberation_payloads = prefer_liberation_payloads
    _server_port = port
    _save_format = (
        save_format
        if save_format in (SAVE_FORMAT_CLASSIC, SAVE_FORMAT_PLAIN_TEXT)
        else SAVE_FORMAT_CLASSIC
    )
    _create_dir_if_needed(save_dir())


def base_path() -> Path:
    global _dcs_saved_game_folder
    assert _dcs_saved_game_folder
    return _create_dir_if_needed(Path(_dcs_saved_game_folder))


def debug_dir() -> Path:
    return _create_dir_if_needed(base_path() / "Retribution" / "Debug")


def factions_dir() -> Path:
    return _create_dir_if_needed(base_path() / "Retribution" / "Factions")


def groups_dir() -> Path:
    return _create_dir_if_needed(base_path() / "Retribution" / "Groups")


def layouts_dir() -> Path:
    return _create_dir_if_needed(base_path() / "Retribution" / "Layouts")


def waypoint_debug_directory() -> Path:
    return _create_dir_if_needed(debug_dir() / "Waypoints")


def settings_dir() -> Path:
    return _create_dir_if_needed(base_path() / "Retribution" / "Settings")


def forced_options_path() -> Path:
    return _create_dir_if_needed(base_path() / "Retribution") / "forced_options.lua"


def airwing_dir() -> Path:
    return _create_dir_if_needed(base_path() / "Retribution" / "AirWing")


def kneeboards_dir() -> Path:
    return _create_dir_if_needed(base_path() / "Retribution" / "Kneeboards")


def payloads_dir(backup: bool = False) -> Path:
    payloads = base_path() / "MissionEditor" / "UnitPayloads"
    if backup:
        return _create_dir_if_needed(payloads / "_retribution_backups")
    return _create_dir_if_needed(payloads)


def prefer_liberation_payloads() -> bool:
    global _prefer_liberation_payloads
    return _prefer_liberation_payloads


def user_custom_weapon_injections_dir() -> Path:
    return _create_dir_if_needed(base_path() / "Retribution" / "WeaponInjections")


def save_dir() -> Path:
    return _create_dir_if_needed(base_path() / "Retribution" / "Saves")


def pre_pretense_backups_dir() -> Path:
    return _create_dir_if_needed(save_dir() / "PrePretenseBackups")


def server_port() -> int:
    global _server_port
    return _server_port


def save_format() -> str:
    global _save_format
    return _save_format


def use_plain_text_saves() -> bool:
    return save_format() == SAVE_FORMAT_PLAIN_TEXT


def _temporary_save_file() -> str:
    suffix = ".json" if use_plain_text_saves() else ".retribution"
    return str(save_dir() / f"tmpsave{suffix}")


def _autosave_path() -> str:
    suffix = ".json" if use_plain_text_saves() else ".retribution"
    return str(save_dir() / f"autosave{suffix}")


def _text_save_path(path: str) -> str:
    return str(Path(path).with_suffix(".json"))


def mission_path_for(name: str) -> Path:
    return base_path() / "Missions" / name


def load_game(path: str) -> Optional[Game]:
    try:
        if Path(path).suffix.lower() == ".json":
            _register_jsonpickle_handlers()
            with open(path, "r", encoding="utf-8") as f:
                raw_text = _apply_json_migration_map(f.read())
                try:
                    wrapper = json.loads(raw_text)
                except json.JSONDecodeError:
                    wrapper = None
                if isinstance(wrapper, dict) and "pickle" in wrapper:
                    try:
                        payload = base64.b64decode(wrapper["pickle"])
                        save = MigrationUnpickler(io.BytesIO(payload)).load()
                    except Exception:
                        logging.exception("Failed to load JSON pickle payload")
                        raise
                else:
                    try:
                        save = jsonpickle.decode(raw_text, keys=True)
                    except TypeError as exc:
                        if "unhashable type" in str(exc):
                            logging.warning(
                                "JSON save load fell back to string keys: %s", exc
                            )
                            try:
                                data = json.loads(raw_text)
                                data = _coerce_unhashable_sets(data)
                                save = jsonpickle_unpickler.Unpickler(
                                    keys=True
                                ).restore(data)
                            except Exception:
                                save = jsonpickle.decode(raw_text, keys=False)
                        else:
                            raise
            save.savepath = path
            return save
        with open(path, "rb") as f:
            save = MigrationUnpickler(f).load()
            save.savepath = path
            return save
    except Exception:
        logging.exception("Invalid Save game")
        return None


def save_game(game: Game) -> bool:
    with logged_duration("Saving game"):
        try:
            if use_plain_text_saves():
                game.savepath = str(Path(game.savepath).with_suffix(".json"))
                _export_text_save(game, game.savepath)
            else:
                with open(_temporary_save_file(), "wb") as f:
                    data = _unload_static_data(game)
                    pickle.dump(game, f)
                    _restore_static_data(game, data)
                shutil.copy(_temporary_save_file(), game.savepath)
            return True
        except Exception:
            logging.exception("Could not save game")
            return False


def _restore_static_data(game: Game, data: dict[str, Any]) -> None:
    game.theater.landmap = data["landmap"]


def _unload_static_data(game: Game) -> dict[str, Any]:
    landmap = game.theater.landmap
    game.theater.landmap = None
    return {
        "landmap": landmap,
    }


def autosave(game: Game) -> bool:
    """
    Autosave to the autosave location
    :param game: Game to save
    :return: True if saved successfully
    """
    try:
        if use_plain_text_saves():
            _export_text_save(game, _autosave_path())
        else:
            with open(_autosave_path(), "wb") as f:
                data = _unload_static_data(game)
                pickle.dump(game, f)
                _restore_static_data(game, data)
        return True
    except Exception:
        logging.exception("Could not save game")
        return False


def _export_text_save(game: Game, path: str) -> None:
    """Export a git-friendly JSON sidecar for a binary save."""
    _register_jsonpickle_handlers()
    data = _unload_static_data(game)
    try:
        pickler = jsonpickle_pickler.Pickler(
            unpicklable=True, make_refs=True, keys=True
        )
        payload = pickler.flatten(game)
        binary_payload = pickle.dumps(game, protocol=pickle.HIGHEST_PROTOCOL)
        wrapper = {
            "format": "jsonpickle",
            "payload": payload,
            "pickle": base64.b64encode(binary_payload).decode("ascii"),
        }
        encoded = json.dumps(wrapper, sort_keys=True, separators=(",", ":"))
        json_path = _text_save_path(path)
        Path(json_path).parent.mkdir(parents=True, exist_ok=True)
        with open(json_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(encoded)
            f.write("\n")
    except Exception:
        logging.exception("Could not export text save")
        raise
    finally:
        _restore_static_data(game, data)
