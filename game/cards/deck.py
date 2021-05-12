import random
from typing import Generic, List, Dict, TypeVar

T = TypeVar('T')


class Deck(Generic[T]):

    def __init__(self, cards: List[T]):
        self._deck = [*cards]
        self._discard = []

    def refill(self):
        random.shuffle(self._discard)
        self._deck += self._discard
        self._discard = []

    def shuffle(self):
        random.shuffle(self._deck)

    def take_top(self) -> T:
        if self.is_empty():
            return None
        return self._deck.pop()

    def take_bottom(self) -> T:
        if self.is_empty():
            return None
        return self._deck.pop(0)

    def is_empty(self) -> bool:
        return len(self._deck) == 0

    def remaining(self) -> int:
        return len(self._deck)

    def discard(self, card: T):
        self._discard.append(card)

    def deck_state(self) -> Dict[str, any]:
        return {
            "count": len(self._deck),
            "discarded": len(self._discard),
            "discard": [card.value for card in self._discard],
        }
