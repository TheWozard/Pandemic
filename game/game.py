from game.cards.infection_deck import create_infection_deck
from game.cards.player_deck import create_player_deck
from game.node import Node
from game.params import Cities
from typing import Dict

class Game:
    def __init__(self, board: Dict[Cities, Node]):
        self._board = board
        self._player_deck = create_player_deck(board.keys(), 2)
        self._infection_deck = create_infection_deck(board.keys(), 1)

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

    def board_state(self) -> Dict[str,Dict[str,int]]:
        board = {}
        for city in self._board:
            board[city.value] = self._board[city].node_state()
        return {
            "board": board,
            "decks": {
                "player": self._player_deck.deck_state(),
                "infection": self._infection_deck.deck_state(),
            }
        }