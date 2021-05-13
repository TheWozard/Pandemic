from typing import Dict, List

from game.cards.infection_deck import create_infection_deck
from game.cards.player_deck import create_player_deck
from game.node import Node
from game.params import Cities, Diseases


class Game:
    def __init__(self, board: Dict[Cities, Node], diseases: List[Diseases], infection_rates: List[int], starting_city: Cities):

        self._board = board
        self._player_deck = create_player_deck(
            board.keys(), infection_cards=len(infection_rates), guarantied_count=9)
        self._infection_deck = create_infection_deck(board.keys())

        self._research_stations = [starting_city]

        for _ in range(3):
            city = self._infection_deck.take_top()
            board[city].set_disease(3)
            self._infection_deck.discard(city)

        for _ in range(3):
            city = self._infection_deck.take_top()
            board[city].set_disease(2)
            self._infection_deck.discard(city)

        for _ in range(3):
            city = self._infection_deck.take_top()
            board[city].set_disease(1)
            self._infection_deck.discard(city)

        self._cures = {}
        for disease in diseases:
            self._cures[disease] = False

        self._infection_index = 0
        self._infection_rates = infection_rates

        # TODO: Players and their cards
        # TODO: Infection Rate Tracking
        # TODO: Outbreaks Tracker
        # TODO: Cube Counting
        # TODO: Research Stations

    def board_state(self) -> Dict[str, Dict[str, int]]:
        board = {}
        for city in self._board:
            board[city.value] = self._board[city].node_state()
        return {
            "board": board,
            "info": {
                "cures": { disease.value:self._cures[disease] for disease in self._cures },
                "infections": self._infection_index,
                "infection_rate": self._infection_rates[self._infection_index],
                "infection_tracker": self._infection_rates,
            },
            "decks": {
                "player": self._player_deck.deck_state(),
                "infection": self._infection_deck.deck_state(),
            }
        }
