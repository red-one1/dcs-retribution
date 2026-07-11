from __future__ import annotations

from types import SimpleNamespace
from typing import cast

from game.ato.flight import Flight
from game.ato.flightplans.afac import AfacFlightPlan
from game.ato.flightplans.flightplanbuildertypes import FlightPlanBuilderTypes
from game.ato.flighttype import FlightType
from game.dcs.aircrafttype import AircraftType
from game.settings.settings import Settings


class _StubFlight:
    """Minimal flight exposing only what ``for_flight`` reads for AFAC."""

    flight_type = FlightType.AFAC


def test_afac_is_registered_flight_plan() -> None:
    builder = FlightPlanBuilderTypes.for_flight(cast(Flight, _StubFlight()))
    assert builder is AfacFlightPlan.builder_type()


def test_auto_afac_for_cas_enabled_by_default() -> None:
    assert Settings().auto_afac_for_cas is True


def test_afac_flight_type_round_trips_by_name() -> None:
    # flight_type is persisted to saves by value, so the name must round-trip.
    assert FlightType.from_name(FlightType.AFAC.value) is FlightType.AFAC


def test_afac_capability_enriched_from_cas() -> None:
    # A CAS-capable airframe should gain AFAC capability.
    fake = SimpleNamespace(
        task_priorities={FlightType.CAS: 650}, carrier_capable=False, price=4
    )
    AircraftType.__post_init__(cast(AircraftType, fake))
    assert FlightType.AFAC in fake.task_priorities


def test_afac_priority_favours_cheaper_aircraft() -> None:
    # AFAC priority is derived inversely from price, so a cheaper airframe should
    # outrank a more expensive one for the task.
    cheap = SimpleNamespace(
        task_priorities={FlightType.CAS: 650}, carrier_capable=False, price=4
    )
    expensive = SimpleNamespace(
        task_priorities={FlightType.CAS: 650}, carrier_capable=False, price=40
    )
    AircraftType.__post_init__(cast(AircraftType, cheap))
    AircraftType.__post_init__(cast(AircraftType, expensive))
    assert (
        cheap.task_priorities[FlightType.AFAC]
        > expensive.task_priorities[FlightType.AFAC]
    )


def test_afac_capability_not_enriched_without_cas() -> None:
    # Aircraft with no CAS capability must not gain AFAC.
    fake = SimpleNamespace(
        task_priorities={FlightType.STRIKE: 3}, carrier_capable=False, price=20
    )
    AircraftType.__post_init__(cast(AircraftType, fake))
    assert FlightType.AFAC not in fake.task_priorities
