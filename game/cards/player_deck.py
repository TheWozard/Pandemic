from typing import List
import random
import math

from game.cards.deck import Deck
from game.params import Cities, SpecialCards

def create_player_deck(cities: List[Cities], duplicates: int, infection_cards: int, guarantied_count: int) -> Deck[Cities]:
    # TODO: Action Cards
    cards = [ele for ele in cities for _ in range(duplicates)]
    random.shuffle(cards)
    starting_cards = cards[:guarantied_count]
    cards = cards[guarantied_count:]
    deck = Deck([])

    for x in range(infection_cards):
        set_size = math.ceil(len(cards)/(infection_cards-x))
        for _ in range(set_size):
            deck.discard(cards.pop())
        deck.discard(SpecialCards.Infection)
        deck.refill()

    for card in starting_cards:
        deck.discard(card)
    
    deck.refill()

    return deck