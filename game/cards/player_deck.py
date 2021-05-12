from typing import List
import random
import math

from game.cards.deck import Deck
from game.params import Cities, SpecialCards

def create_player_deck(cities: List[Cities], duplicates: int, infection_cards: int, hands: int, hand_size: int) -> Deck[Cities]:
    # TODO: Action Cards
    # TODO: Infection Cards
    cards = [ele for ele in cities for _ in range(duplicates)]
    random.shuffle(cards)
    starting_cards = []
    deck = Deck([])

    for x in range(infection_cards):
        for _ in range(math.floor(cards/(infection_cards-x))):
            deck.discard(cards.pop())
        deck.discard(SpecialCards.Infection)
        deck.refill()

    return deck