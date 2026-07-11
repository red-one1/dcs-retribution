from __future__ import annotations

from datetime import timedelta
from typing import Type

from game.ato.flightplans.ibuilder import IBuilder
from game.ato.flightplans.invalidobjectivelocation import InvalidObjectiveLocation
from game.ato.flightplans.patrolling import PatrollingFlightPlan, PatrollingLayout
from game.ato.flightplans.waypointbuilder import WaypointBuilder
from game.theater import FrontLine
from game.utils import Distance, Speed, meters, nautical_miles

# How far behind the friendly side of the FLOT the FAC orbits, so it stays clear
# of the contact line while designating targets.
AFAC_STANDOFF = nautical_miles(6)


class AfacFlightPlan(PatrollingFlightPlan[PatrollingLayout]):
    """Airborne FAC flight plan.

    Unlike the auto-spawned immortal JTAC drone, an AFAC flight takes off from an
    airfield, transits to the front line and only begins its FAC task once on
    station, orbiting a race-track behind the friendly side of the FLOT.
    """

    @staticmethod
    def builder_type() -> Type[Builder]:
        return Builder

    @property
    def patrol_duration(self) -> timedelta:
        return self.flight.coalition.doctrine.cas_duration

    @property
    def patrol_speed(self) -> Speed:
        return self.flight.unit_type.preferred_patrol_speed(
            self.layout.patrol_start.alt
        )

    @property
    def engagement_distance(self) -> Distance:
        # FAC target designation is handled by the autolase script, not by a
        # Search Then Engage task, so no engagement range is required.
        return meters(0)


class Builder(IBuilder[AfacFlightPlan, PatrollingLayout]):
    def layout(self) -> PatrollingLayout:
        location = self.package.target
        if not isinstance(location, FrontLine):
            raise InvalidObjectiveLocation(self.flight.flight_type, location)

        from game.missiongenerator.frontlineconflictdescription import (
            FrontLineConflictDescription,
        )

        bounds = FrontLineConflictDescription.frontline_bounds(location, self.theater)

        # Stand off toward friendly territory so the FAC orbits behind the FLOT
        # rather than directly over the contact line.
        friendly_cp = location.control_point_friendly_to(self.coalition.player)
        standoff = AFAC_STANDOFF.meters
        heading_to_friendly = location.position.heading_between_point(
            friendly_cp.position
        )
        patrol_start = bounds.left_position.point_from_heading(
            heading_to_friendly, standoff
        )
        patrol_end = bounds.right_position.point_from_heading(
            heading_to_friendly, standoff
        )

        # Orbit the closest end first.
        start_distance = patrol_start.distance_to_point(self.flight.departure.position)
        end_distance = patrol_end.distance_to_point(self.flight.departure.position)
        if end_distance < start_distance:
            patrol_start, patrol_end = patrol_end, patrol_start

        builder = WaypointBuilder(self.flight)
        altitude = builder.get_patrol_altitude
        racetrack = builder.race_track(patrol_start, patrol_end, altitude)

        return PatrollingLayout(
            departure=builder.takeoff(self.flight.departure),
            nav_to=builder.nav_path(
                self.flight.departure.position, patrol_start, altitude
            ),
            nav_from=builder.nav_path(
                patrol_end, self.flight.arrival.position, altitude
            ),
            patrol_start=racetrack[0],
            patrol_end=racetrack[1],
            arrival=builder.land(self.flight.arrival),
            divert=builder.divert(self.flight.divert),
            bullseye=builder.bullseye(),
            custom_waypoints=list(),
        )

    def build(self, dump_debug_info: bool = False) -> AfacFlightPlan:
        return AfacFlightPlan(self.flight, self.layout())
