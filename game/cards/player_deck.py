from typing import List

from game.cards.deck import Deck
from game.params import Cities

def create_player_deck(cities: List[Cities], duplicates: int) -> Deck[Cities]:
    # TODO: Action Cards
    cards = [ele for ele in cities for _ in range(duplicates)]
    deck = Deck(cards)

    return deck