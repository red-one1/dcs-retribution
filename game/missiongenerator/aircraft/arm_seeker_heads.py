from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
import math
from typing import Optional, Iterable, TYPE_CHECKING

from game.data.units import UnitClass
from game.theater import MissionTarget, TheaterGroundObject
from game.theater.theatergroup import TheaterUnit
from game.utils import NM_TO_METERS

if TYPE_CHECKING:
    from game.ato.flight import Flight
    from game.theater.theatergroundobject import IadsGroundObject


@dataclass(frozen=True)
class SeekerHead:
    name: str
    rfgu_type: int
    rf_lower_hz: int
    rf_upper_hz: int


SEEKER_HEADS: dict[str, SeekerHead] = {
    "Mk 22": SeekerHead("Mk 22", 1, 4_800_000_000, 5_200_000_000),
    "Mk 23": SeekerHead("Mk 23", 2, 2_000_000_000, 4_000_000_000),
    "Mk 24 Mod 5": SeekerHead("Mk 24 Mod 5", 3, 2_650_000_000, 3_150_000_000),
    "Mk 24 Mod 34": SeekerHead("Mk 24 Mod 34", 4, 2_500_000_000, 3_500_000_000),
    "Mk 25": SeekerHead("Mk 25", 5, 4_000_000_000, 6_000_000_000),
    "Mk 36": SeekerHead("Mk 36", 6, 7_900_000_000, 9_600_000_000),
    "Mk 37": SeekerHead("Mk 37", 7, 800_000_000, 1_000_000_000),
    "Mk 49 Mod 0": SeekerHead("Mk 49 Mod 0", 8, 6_000_000_000, 10_000_000_000),
    "Mk 49 Mod 1": SeekerHead("Mk 49 Mod 1", 9, 6_000_000_000, 10_000_000_000),
    "Mk 50": SeekerHead("Mk 50", 10, 2_000_000_000, 6_000_000_000),
}

SAM_TO_SEEKER: dict[str, str] = {
    "SA-2": "Mk 22",
    "SA-3": "Mk 36",
    "SA-5": "Mk 23",
    "SA-6": "Mk 49 Mod 0",
    "SA-8": "Mk 37",
    "SA-10": "Mk 23",
    "SA-11": "Mk 36",
    "SA-13": "Mk 22",
    "SA-15": "Mk 22",
    "SA-19": "Mk 23",
    "EWR": "Mk 22",
}

SAM_SEEKER_BY_ROLE: dict[str, dict[str, str]] = {
    "SA-2": {"tr": "Mk 22", "sr": "Mk 37"},
    "SA-3": {"tr": "Mk 36", "sr": "Mk 37"},
    "SA-5": {"tr": "Mk 49 Mod 0", "sr": "Mk 23"},
    "SA-6": {"tr": "Mk 49 Mod 0", "sr": "Mk 37"},
    "SA-8": {"sr": "Mk 37"},
    "SA-10": {"tr": "Mk 36", "sr": "Mk 23"},
    "SA-11": {"tr": "Mk 36", "sr": "Mk 23"},
    "SA-13": {"tr": "Mk 22"},
    "SA-15": {"tr": "Mk 22", "sr": "Mk 23"},
    "SA-19": {"sr": "Mk 23"},
}

SAM_PRIORITY: tuple[str, ...] = (
    "SA-2",
    "SA-3",
    "SA-5",
    "SA-6",
    "SA-8",
    "SA-10",
    "SA-11",
    "SA-13",
    "SA-15",
    "SA-19",
)

RADAR_NAME_TO_ROLE_SEEKER: dict[str, tuple[str, str]] = {
    "fan song": ("tr", "Mk 22"),
    "fire can": ("tr", "Mk 24 Mod 5"),
    "low blow": ("tr", "Mk 36"),
    "straight flush": ("tr", "Mk 49 Mod 0"),
    "tin shield": ("sr", "Mk 23"),
    "flat face": ("sr", "Mk 37"),
    "big bird": ("sr", "Mk 23"),
    "clam shell": ("sr", "Mk 23"),
    "dog ear": ("sr", "Mk 22"),
}


def is_shrike_or_standard(weapon_name: str) -> bool:
    normalized = weapon_name.upper()
    return "AGM-45" in normalized or "SHRIKE" in normalized or "AGM-78" in normalized


def seeker_head_for_target(target: MissionTarget) -> Optional[SeekerHead]:
    return _seeker_for_target(target)


def seeker_heads_for_target_roles(
    target: MissionTarget,
) -> tuple[Optional[SeekerHead], Optional[SeekerHead]]:
    if isinstance(target, TheaterGroundObject):
        tr_head, sr_head = _seeker_heads_from_units(target)
        if tr_head is not None or sr_head is not None:
            return tr_head, sr_head

    sam_type = _sam_type_for_target(target)
    if sam_type is None:
        return None, None
    roles = SAM_SEEKER_BY_ROLE.get(sam_type, {})
    tr_head = SEEKER_HEADS.get(roles.get("tr", "")) if roles.get("tr") else None
    sr_head = SEEKER_HEADS.get(roles.get("sr", "")) if roles.get("sr") else None
    return tr_head, sr_head


def auto_seeker_for_pylon(
    target: MissionTarget, shrike_pylons: list[int], pylon_number: int
) -> Optional[SeekerHead]:
    tr_head, sr_head = seeker_heads_for_target_roles(target)
    if tr_head is not None and sr_head is not None and shrike_pylons:
        ordered = sorted(shrike_pylons)
        tr_count = len(ordered) // 2
        if len(ordered) % 2 == 1:
            tr_count += 1
        if pylon_number in ordered[:tr_count]:
            return tr_head
        return sr_head

    if tr_head is not None:
        return tr_head
    if sr_head is not None:
        return sr_head
    return seeker_head_for_target(target)


def auto_seeker_for_pylon_on_route(
    flight: Flight, shrike_pylons: list[int], pylon_number: int, radius_nm: float = 50
) -> Optional[SeekerHead]:
    tr_head, sr_head = seeker_heads_for_sead_escort(flight, radius_nm)
    if tr_head is not None and sr_head is not None and shrike_pylons:
        ordered = sorted(shrike_pylons)
        tr_count = len(ordered) // 2
        if len(ordered) % 2 == 1:
            tr_count += 1
        if pylon_number in ordered[:tr_count]:
            return tr_head
        return sr_head
    if tr_head is not None:
        return tr_head
    if sr_head is not None:
        return sr_head
    return None


def seeker_heads_for_sead_escort(
    flight: Flight, radius_nm: float = 50
) -> tuple[Optional[SeekerHead], Optional[SeekerHead]]:
    tr_counts: Counter[str] = Counter()
    sr_counts: Counter[str] = Counter()

    path = [w.position for w in flight.flight_plan.waypoints]
    if len(path) < 2:
        return seeker_heads_for_target_roles(flight.package.target)

    radius_m = radius_nm * NM_TO_METERS
    for go in flight.coalition.game.theater.ground_objects:
        if go.is_friendly(flight.coalition.player):
            continue
        if not _is_iads_ground_object(go):
            continue
        if go.alive_unit_count == 0:
            continue
        if _distance_to_path(go.position.x, go.position.y, path) > radius_m:
            continue
        tr_head, sr_head = _seeker_heads_from_units(go)
        if tr_head is not None:
            tr_counts[tr_head.name] += 1
        if sr_head is not None:
            sr_counts[sr_head.name] += 1

    tr_head = _most_common_head(tr_counts)
    sr_head = _most_common_head(sr_counts)
    if tr_head is None and sr_head is None:
        return seeker_heads_for_target_roles(flight.package.target)
    return tr_head, sr_head


def seeker_head_for_settings(settings: dict[str, int]) -> Optional[SeekerHead]:
    rfgu_type = settings.get("NFP_rfgu_type")
    if rfgu_type is None:
        return None
    for seeker in SEEKER_HEADS.values():
        if seeker.rfgu_type == rfgu_type:
            return seeker
    return None


def seeker_settings_for_head(seeker: SeekerHead) -> dict[str, int]:
    return {
        "NFP_rfgu_type": seeker.rfgu_type,
        "rf_lower_limit_ctrl_Mk22Mod2": seeker.rf_lower_hz,
        "rf_upper_limit_ctrl_Mk22Mod2": seeker.rf_upper_hz,
    }


def seeker_settings_for_target(target: MissionTarget) -> Optional[dict[str, int]]:
    seeker = _seeker_for_target(target)
    if seeker is None:
        return None
    return seeker_settings_for_head(seeker)


def _seeker_for_target(target: MissionTarget) -> Optional[SeekerHead]:
    if not isinstance(target, TheaterGroundObject):
        return None

    for unit in _iter_relevant_units(target):
        seeker = _seeker_for_unit(unit)
        if seeker is not None:
            return seeker

    sam_type = _sam_type_for_target(target)
    if sam_type is None:
        return None
    seeker_name = SAM_TO_SEEKER.get(sam_type)
    if seeker_name is None:
        return None
    return SEEKER_HEADS[seeker_name]


def _seeker_for_unit(unit: TheaterUnit) -> Optional[SeekerHead]:
    display = _unit_display_name(unit).lower()
    for radar_name, (_, seeker_name) in RADAR_NAME_TO_ROLE_SEEKER.items():
        if radar_name in display:
            return SEEKER_HEADS[seeker_name]
    return None


def _seeker_heads_from_units(
    target: TheaterGroundObject,
) -> tuple[Optional[SeekerHead], Optional[SeekerHead]]:
    tr_head = None
    sr_head = None
    for unit in _iter_relevant_units(target):
        display = _unit_display_name(unit).lower()
        for radar_name, (role, seeker_name) in RADAR_NAME_TO_ROLE_SEEKER.items():
            if radar_name in display:
                seeker = SEEKER_HEADS[seeker_name]
                if role == "tr" and tr_head is None:
                    tr_head = seeker
                elif role == "sr" and sr_head is None:
                    sr_head = seeker
        if tr_head is not None and sr_head is not None:
            break
    return tr_head, sr_head


def _most_common_head(counter: Counter[str]) -> Optional[SeekerHead]:
    if not counter:
        return None
    name, _ = sorted(counter.items(), key=lambda item: (-item[1], item[0]))[0]
    return SEEKER_HEADS.get(name)


def _distance_to_path(px: float, py: float, path: list) -> float:
    min_dist = math.inf
    for start, end in zip(path, path[1:]):
        dist = _distance_point_to_segment(px, py, start.x, start.y, end.x, end.y)
        if dist < min_dist:
            min_dist = dist
    return min_dist


def _distance_point_to_segment(
    px: float, py: float, ax: float, ay: float, bx: float, by: float
) -> float:
    dx = bx - ax
    dy = by - ay
    if dx == 0 and dy == 0:
        return math.hypot(px - ax, py - ay)
    t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)
    t = max(0.0, min(1.0, t))
    closest_x = ax + t * dx
    closest_y = ay + t * dy
    return math.hypot(px - closest_x, py - closest_y)


def _is_iads_ground_object(go: TheaterGroundObject) -> bool:
    from game.theater.theatergroundobject import IadsGroundObject

    return isinstance(go, IadsGroundObject)


def _sam_type_for_target(target: MissionTarget) -> Optional[str]:
    if not isinstance(target, TheaterGroundObject):
        return None

    matches: set[str] = set()
    has_ewr = False
    for unit in _iter_relevant_units(target):
        unit_type = unit.unit_type
        if (
            unit_type is not None
            and unit_type.unit_class is UnitClass.EARLY_WARNING_RADAR
        ):
            has_ewr = True
        display = _unit_display_name(unit)
        for match in re.findall(r"SA-\d+", display):
            matches.add(match)

    for sam in SAM_PRIORITY:
        if sam in matches:
            return sam

    if has_ewr:
        return "EWR"

    return None


def _iter_relevant_units(target: TheaterGroundObject) -> Iterable[TheaterUnit]:
    return (unit for unit in target.units if unit.alive)


def _unit_display_name(unit: TheaterUnit) -> str:
    unit_type = unit.unit_type
    if unit_type is not None:
        return unit_type.display_name
    return unit.type.name or unit.type.id
