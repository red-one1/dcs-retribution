from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from PySide6.QtWidgets import QHBoxLayout, QGroupBox, QPushButton

import qt_ui.uiconstants as CONST
from game import Game
from game.income import Income
from qt_ui.windows.finances.QFinancesMenu import QFinancesMenu

if TYPE_CHECKING:
    from qt_ui.models import GameModel


class QBudgetBox(QGroupBox):
    """
    UI Component to display current budget and player's money
    """

    def __init__(self, game: Optional[Game], game_model: Optional[GameModel] = None):
        super(QBudgetBox, self).__init__("Budget")

        self.game = game
        self.game_model = game_model

        self.finances = QPushButton()
        self.finances.setDisabled(True)
        self.finances.setProperty("style", "btn-primary")
        self.finances.setIcon(CONST.ICONS["Money"])
        self.finances.clicked.connect(self.openFinances)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.finances)
        self.setLayout(self.layout)

    def setBudget(self, budget, reward):
        """
        Set the money amount to display
        :param budget: Current money available
        :param reward: Planned reward for next turn
        """
        self.finances.setText(
            str(round(budget, 2)) + "M (+" + str(round(reward, 2)) + "M)"
        )

    def setGame(self, game):
        if game is None:
            return

        self.game = game
        if self.game_model is not None:
            player = self.game_model.current_player
        else:
            from game.theater.player import Player

            player = Player.BLUE
        self.setBudget(
            self.game.coalition_for(player).budget,
            Income(self.game, player=player).total,
        )
        self.finances.setEnabled(True)

    def openFinances(self):
        if self.game_model is not None:
            self.subwindow = QFinancesMenu(
                self.game, player=self.game_model.current_player
            )
        else:
            self.subwindow = QFinancesMenu(self.game)
        self.subwindow.show()
