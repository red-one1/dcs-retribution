import logging

from dcs.point import MovingPoint
from dcs.task import (
    EngageTargets,
    OptROE,
    SetUnlimitedFuelCommand,
    Targets,
)

from game.ato import FlightType
from game.ato.flightplans.patrolling import PatrollingFlightPlan
from game.utils import nautical_miles
from .pydcswaypointbuilder import PydcsWaypointBuilder


class RaceTrackEndBuilder(PydcsWaypointBuilder):
    def add_tasks(self, waypoint: MovingPoint) -> None:
        # Unlimited fuel option : enable at racetrack end. Must be first option to work.
        if self.flight.squadron.coalition.game.settings.ai_unlimited_fuel:
            waypoint.tasks.insert(0, SetUnlimitedFuelCommand(True))

        # Disable Offensive Jamming at Racetrack End
        if self.flight.flight_type == FlightType.AEWC:
            # Stop Defensive Jamming for all AWACS flights
            settings = self.flight.coalition.game.settings
            ai_jammer = settings.plugin_option("ewrj.ai_jammer_enabled")
            if settings.plugins.get("ewrj") and ai_jammer:
                self.defensive_jamming(waypoint, "stop")
                self.offensive_jamming(waypoint, "stop")

        if self.flight.flight_type == FlightType.TARCAP:
            # TARCAP self-defense after patrol: air-only engagement within 20nm.
            waypoint.tasks.append(OptROE(value=OptROE.Values.OpenFireWeaponFree))
            waypoint.tasks.append(
                EngageTargets(
                    max_distance=int(nautical_miles(20).meters),
                    targets=[Targets.All.Air],
                )
            )

    def build(self) -> MovingPoint:
        waypoint = super().build()

        if not isinstance(self.flight.flight_plan, PatrollingFlightPlan):
            flight_plan_type = self.flight.flight_plan.__class__.__name__
            logging.error(
                f"Cannot create race track for {self.flight} because "
                f"{flight_plan_type} does not define a patrol."
            )
            return waypoint

        self.waypoint.departure_time = self.flight.flight_plan.patrol_end_time
        return waypoint
