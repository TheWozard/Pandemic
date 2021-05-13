from typing import List

from game.cards.deck import Deck
from game.params import Cities

def create_infection_deck(cities: List[Cities]) -> Deck[Cities]:
    deck = Deck(cities)

    return deck
