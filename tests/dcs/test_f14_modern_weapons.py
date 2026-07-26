"""Regression tests for the F-14 Modern Weapons mod injection.

The mod (by DSplayer) is a *weapons* mod: it grafts modern ordnance onto the
stock Heatblur F-14 rather than adding a new airframe, so support is implemented
as pydcs pylon injection (``pydcs_extensions/f14_modern_weapons``). These tests
pin the mod author's published loadout matrix:

* the glove pylons (pydcs P2/P9) gain AMRAAM/AIM-9X/AIM-54C+/AIM-174B/HARM/
  Maverick/Harpoon, and the belly stations (P4-P7) gain AMRAAM/AIM-54C+/Skipper,
* JDAM (GBU-38/54) is *F-14B(U) only* and therefore must **not** appear on the
  stock F-14B belly, and
* the pure-AI ``F-14A`` is left untouched by the mod.

Each test injects, asserts, and then ejects, and a dedicated test proves the
round-trip restores the original pylons — so reverting the feature fails loudly.
"""

from __future__ import annotations

from typing import Any, Iterator

import pytest

# Import a game module first so pydcs_extensions' package import order is resolved
# (importing pydcs_extensions standalone hits a known circular import via game).
from game.theater.start_generator import ModSettings  # noqa: F401
from dcs.planes import (
    F_14A,
    F_14B,
    F_14A_95_GR,
    F_14A_135_GR,
    F_14A_135_GR_Early,
)
from dcs.weapons_data import weapon_ids

from pydcs_extensions import inject_F14ModernWeapons, eject_F14ModernWeapons

# CLSIDs the mod adds, taken from the modded pydcs export / author loadout chart.
SHOULDER_AMRAAM_A = "{SHOULDER AIM-120A}"
SHOULDER_HARM = "{SHOULDER_AGM_88}"
SHOULDER_AIM_174B_L = "{SHOULDER AIM_174B L}"
BELLY_AMRAAM_A = "{AIM_120A}"
BELLY_SKIPPER = "{BRU-32 AGM-123}"
# JDAM is F-14BU-only per the author's chart; it must never reach the stock F-14B.
BELLY_JDAM_GBU38 = "{BRU-32 GBU-38}"


def _pylon_clsids(pylon: Any) -> set[str]:
    out: set[str] = set()
    for name, value in vars(pylon).items():
        if name.startswith("__"):
            continue
        if isinstance(value, tuple) and len(value) == 2 and isinstance(value[1], dict):
            clsid = value[1].get("clsid")
            if clsid:
                out.add(clsid)
    return out


def _all_clsids(plane: Any) -> set[str]:
    clsids: set[str] = set()
    for num in plane.pylons:
        pylon = getattr(plane, f"Pylon{num}", None)
        if pylon is not None:
            clsids |= _pylon_clsids(pylon)
    return clsids


@pytest.fixture()
def injected() -> Iterator[None]:
    inject_F14ModernWeapons()
    try:
        yield
    finally:
        eject_F14ModernWeapons()


@pytest.mark.parametrize(
    "plane",
    [F_14B, F_14A_95_GR, F_14A_135_GR, F_14A_135_GR_Early],
)
def test_glove_pylons_gain_modern_air_to_air(plane: Any, injected: None) -> None:
    # P2 (1B) and P9 (8B) are the wing-glove Phoenix pylons.
    for num in (2, 9):
        clsids = _pylon_clsids(getattr(plane, f"Pylon{num}"))
        assert SHOULDER_AMRAAM_A in clsids
        assert SHOULDER_HARM in clsids
        assert SHOULDER_AIM_174B_L in clsids or "{SHOULDER AIM_174B R}" in clsids


@pytest.mark.parametrize(
    "plane",
    [F_14B, F_14A_95_GR, F_14A_135_GR, F_14A_135_GR_Early],
)
def test_belly_stations_gain_amraam_and_skipper(plane: Any, injected: None) -> None:
    # P4-P7 are the belly tunnel stations (physical 3/4/5/6).
    belly = set()
    for num in (4, 5, 6, 7):
        belly |= _pylon_clsids(getattr(plane, f"Pylon{num}"))
    assert BELLY_AMRAAM_A in belly
    assert BELLY_SKIPPER in belly


@pytest.mark.parametrize(
    "plane",
    [F_14B, F_14A_95_GR, F_14A_135_GR, F_14A_135_GR_Early],
)
def test_jdam_is_f14bu_only(plane: Any, injected: None) -> None:
    # GBU-38/54 JDAM is exclusive to the F-14B(U) in the mod's loadout chart, so
    # the stock airframes must not receive it.
    assert BELLY_JDAM_GBU38 not in _all_clsids(plane)


def test_registers_weapon_clsids(injected: None) -> None:
    assert SHOULDER_AMRAAM_A in weapon_ids
    assert SHOULDER_HARM in weapon_ids


def test_ai_f14a_is_untouched() -> None:
    before = _all_clsids(F_14A)
    inject_F14ModernWeapons()
    try:
        assert _all_clsids(F_14A) == before
    finally:
        eject_F14ModernWeapons()


def test_inject_eject_round_trips() -> None:
    baseline = {
        num: _pylon_clsids(getattr(F_14B, f"Pylon{num}")) for num in F_14B.pylons
    }
    inject_F14ModernWeapons()
    injected = {
        num: _pylon_clsids(getattr(F_14B, f"Pylon{num}")) for num in F_14B.pylons
    }
    eject_F14ModernWeapons()
    restored = {
        num: _pylon_clsids(getattr(F_14B, f"Pylon{num}")) for num in F_14B.pylons
    }

    assert injected != baseline  # the mod actually changed something
    assert restored == baseline  # ejection fully reverses it
