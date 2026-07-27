from __future__ import annotations

from types import SimpleNamespace
from typing import Any, cast

from dcs.mapping import Point
from dcs.point import MovingPoint

from game.missiongenerator.aircraft.flightgroupspawner import (
    ORIENTATION_WAYPOINT_DISTANCE,
    orient_in_air_departure,
)
from game.utils import Heading


def _spawn_point(position: Point) -> MovingPoint:
    point = MovingPoint(position)
    point.alt = 1828  # ~6000 ft
    point.alt_type = "RADIO"
    point.speed = 200.0
    return point


def _group(position: Point, unit_count: int = 2) -> Any:
    units = [SimpleNamespace(heading=0.0) for _ in range(unit_count)]
    return SimpleNamespace(points=[_spawn_point(position)], units=units)


def test_orientation_waypoint_is_inserted_along_runway_heading() -> None:
    spawn_pos = Point(1000.0, 2000.0, cast(Any, None))
    group = _group(spawn_pos)

    orient_in_air_departure(group, Heading.from_degrees(90))

    # The spawn point is preserved and the orientation waypoint is inserted
    # directly after it, ahead of the (not-yet-generated) real waypoints.
    assert len(group.points) == 2
    orientation = group.points[1]
    assert orientation.name == "Orientation WPT"

    expected = spawn_pos.point_from_heading(90, ORIENTATION_WAYPOINT_DISTANCE.meters)
    assert orientation.position.x == expected.x
    assert orientation.position.y == expected.y


def test_orientation_waypoint_copies_spawn_profile() -> None:
    spawn_pos = Point(0.0, 0.0, cast(Any, None))
    group = _group(spawn_pos)
    spawn = group.points[0]

    orient_in_air_departure(group, Heading.from_degrees(270))

    orientation = group.points[1]
    assert orientation.alt == spawn.alt
    assert orientation.alt_type == spawn.alt_type
    assert orientation.speed == spawn.speed
    assert orientation.ETA_locked is False


def test_units_face_the_runway_heading() -> None:
    group = _group(Point(0.0, 0.0, cast(Any, None)), unit_count=3)

    orient_in_air_departure(group, Heading.from_degrees(135))

    assert [unit.heading for unit in group.units] == [135, 135, 135]
