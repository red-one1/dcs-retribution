from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import BaseModel

from game.server.leaflet import LeafletPoint

if TYPE_CHECKING:
    from game import Game
    from game.theater import ControlPoint
    from game.theater.player import Player


class ControlPointJs(BaseModel):
    id: UUID
    name: str
    blue: bool
    position: LeafletPoint
    mobile: bool
    destination: LeafletPoint | None
    sidc: str

    class Config:
        title = "ControlPoint"

    @staticmethod
    def for_control_point(
        control_point: ControlPoint, current_player: Player | None = None
    ) -> ControlPointJs:
        destination = None
        if control_point.target_position is not None:
            destination = control_point.target_position.latlng()
        if control_point.captured.is_blue:
            blue = True
        else:
            blue = False
        # If a current_player is provided, mark as mobile only when the CP
        # belongs to that player.  Without it, fall back to the legacy blue-only
        # behaviour so existing callers keep working.
        if current_player is not None:
            mobile = control_point.moveable and control_point.captured == current_player
        else:
            mobile = control_point.moveable and control_point.captured.is_blue
        return ControlPointJs(
            id=control_point.id,
            name=control_point.name,
            blue=blue,
            position=control_point.position.latlng(),
            mobile=mobile,
            destination=destination,
            sidc=str(control_point.sidc()),
        )

    @staticmethod
    def all_in_game(game: Game) -> list[ControlPointJs]:
        from ..dependencies import GameContext

        current_player = GameContext.get_model().current_player
        return [
            ControlPointJs.for_control_point(cp, current_player)
            for cp in game.theater.controlpoints
        ]
