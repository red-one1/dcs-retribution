import logging
import operator
from typing import Optional

from PySide6.QtWidgets import QComboBox, QHBoxLayout, QLabel, QVBoxLayout, QWidget

from game import Game
from game.ato.flight import Flight
from game.ato.flighttype import FlightType
from game.ato.flightmember import FlightMember
from game.ato.loadouts import Loadout
from game.data.weapons import Pylon, Weapon
from game.missiongenerator.aircraft.arm_seeker_heads import (
    SEEKER_HEADS,
    auto_seeker_for_pylon_on_route,
    auto_seeker_for_pylon,
    is_shrike_or_standard,
    seeker_head_for_settings,
    seeker_head_for_target,
    seeker_heads_for_target_roles,
    seeker_settings_for_head,
)


class QPylonEditor(QWidget):
    def __init__(
        self, game: Game, flight: Flight, flight_member: FlightMember, pylon: Pylon
    ) -> None:
        super().__init__()
        self.flight = flight
        self.flight_member = flight_member
        self.pylon = pylon
        self.game = game
        self.has_added_clean_item = False

        self.weapon_combo = QComboBox()
        self.seeker_combo = QComboBox()
        self.seeker_label = QLabel("Seeker")

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(self.weapon_combo)

        seeker_layout = QHBoxLayout()
        seeker_layout.setContentsMargins(0, 0, 0, 0)
        seeker_layout.addWidget(self.seeker_label)
        seeker_layout.addWidget(self.seeker_combo)

        self.seeker_container = QWidget()
        self.seeker_container.setLayout(seeker_layout)
        main_layout.addWidget(self.seeker_container)
        self.seeker_container.setVisible(False)

        current = self.flight_member.loadout.pylons.get(self.pylon.number)

        self.weapon_combo.addItem("None", None)
        if self.game.settings.restrict_weapons_by_date:
            weapons = pylon.available_on(self.game.date)
        else:
            weapons = pylon.allowed
        allowed = sorted(weapons, key=operator.attrgetter("name"))
        for i, weapon in enumerate(allowed):
            self.weapon_combo.addItem(weapon.name, weapon)
            if current == weapon:
                self.weapon_combo.setCurrentIndex(i + 1)

        self.weapon_combo.currentIndexChanged.connect(self.on_pylon_change)
        self.seeker_combo.currentIndexChanged.connect(self.on_seeker_change)

        self._refresh_seeker_controls()

    def on_pylon_change(self):
        selected: Optional[Weapon] = self.weapon_combo.currentData()
        self.flight_member.loadout.pylons[self.pylon.number] = selected

        if selected is None or not is_shrike_or_standard(selected.name):
            self.flight_member.loadout.set_pylon_settings(self.pylon.number, None)

        if selected is None:
            logging.debug(f"Pylon {self.pylon.number} emptied")
        else:
            logging.debug(f"Pylon {self.pylon.number} changed to {selected.name}")

        self._refresh_seeker_controls()

    def on_seeker_change(self) -> None:
        seeker = self.seeker_combo.currentData()
        if seeker is None:
            self.flight_member.loadout.set_pylon_settings(self.pylon.number, None)
        else:
            self.flight_member.loadout.set_pylon_settings(
                self.pylon.number, seeker_settings_for_head(seeker)
            )

    def weapon_from_loadout(self, loadout: Loadout) -> Optional[Weapon]:
        weapon = loadout.pylons.get(self.pylon.number)
        if weapon is None:
            return None
        # TODO: Fix pydcs to support the <CLEAN> "weapon".
        # These are not exported in the pydcs weapon map, which causes the pydcs pylon
        # exporter to fail to include them in the supported list. Since they aren't
        # known to be compatible (and we can't show them as compatible for *every*
        # pylon, because they aren't), we won't have populated a "Clean" weapon when
        # creating the selection list, so it's not selectable. To work around this, add
        # the item to the list the first time it's encountered for the pylon.
        #
        # A similar hack exists in Pylon to support forcibly equipping this even when
        # it's not known to be compatible.
        if weapon.clsid == "<CLEAN>":
            if not self.has_added_clean_item:
                self.weapon_combo.addItem("Clean", weapon)
                self.has_added_clean_item = True
        return weapon

    def matching_weapon_name(self, loadout: Loadout) -> str:
        if self.game.settings.restrict_weapons_by_date:
            loadout = loadout.degrade_for_date(self.flight.unit_type, self.game.date)
        weapon = self.weapon_from_loadout(loadout)
        if weapon is None:
            return "None"
        return weapon.name

    def set_flight_member(self, flight_member: FlightMember) -> None:
        self.flight_member = flight_member
        self.set_from(self.flight_member.loadout)

    def set_from(self, loadout: Loadout) -> None:
        self.weapon_combo.setCurrentText(self.matching_weapon_name(loadout))
        self._refresh_seeker_controls()

    def _refresh_seeker_controls(self) -> None:
        selected: Optional[Weapon] = self.weapon_combo.currentData()
        if selected is None or not is_shrike_or_standard(selected.name):
            self.seeker_container.setVisible(False)
            return

        self.seeker_combo.blockSignals(True)
        self.seeker_combo.clear()

        shrike_pylons = [
            pylon
            for pylon, weapon in self.flight_member.loadout.pylons.items()
            if weapon is not None and is_shrike_or_standard(weapon.name)
        ]
        if self.flight.flight_type == FlightType.SEAD_ESCORT:
            auto_head = auto_seeker_for_pylon_on_route(
                self.flight, shrike_pylons, self.pylon.number, radius_nm=50
            )
        else:
            auto_head = auto_seeker_for_pylon(
                self.flight.package.target, shrike_pylons, self.pylon.number
            )
        tr_head, sr_head = seeker_heads_for_target_roles(self.flight.package.target)
        if auto_head is not None:
            default_label = f"Auto ({auto_head.name})"
        elif tr_head is not None and sr_head is not None:
            default_label = f"Auto (TR: {tr_head.name} / SR: {sr_head.name})"
        else:
            default_head = seeker_head_for_target(self.flight.package.target)
            default_label = (
                f"Auto ({default_head.name})" if default_head is not None else "Auto"
            )
        self.seeker_combo.addItem(default_label, None)

        for head in SEEKER_HEADS.values():
            self.seeker_combo.addItem(head.name, head)

        settings = self.flight_member.loadout.pylon_settings_for(self.pylon.number)
        if settings is None:
            self.seeker_combo.setCurrentIndex(0)
        else:
            head = seeker_head_for_settings(settings)
            if head is not None:
                self.seeker_combo.setCurrentText(head.name)
            else:
                self.seeker_combo.setCurrentIndex(0)

        self.seeker_combo.blockSignals(False)
        self.seeker_container.setVisible(True)
