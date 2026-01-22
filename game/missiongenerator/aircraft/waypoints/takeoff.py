from dcs.point import MovingPoint
from dcs.task import EngageTargets, OptROE, Targets

from game.ato import FlightType
from game.utils import nautical_miles
from .pydcswaypointbuilder import PydcsWaypointBuilder


class TakeoffPointBuilder(PydcsWaypointBuilder):
    def add_tasks(self, waypoint: MovingPoint) -> None:
        # TARCAP self-defense on departure: allow air-only engagement within 20nm.
        if self.flight.flight_type == FlightType.TARCAP:
            waypoint.tasks.append(OptROE(value=OptROE.Values.OpenFireWeaponFree))
            waypoint.tasks.append(
                EngageTargets(
                    max_distance=int(nautical_miles(20).meters),
                    targets=[Targets.All.Air],
                )
            )
