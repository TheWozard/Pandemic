from typing import List

from game.cards.deck import Deck
from game.params import Cities

def create_infection_deck(cities: List[Cities], duplicates: int) -> Deck[Cities]:
    cards = [ele for ele in cities for _ in range(duplicates)]
    deck = Deck(cards)

    return deck
