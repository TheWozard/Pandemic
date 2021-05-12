import unittest

from game.cards.deck import Deck


class TestDeckMethods(unittest.TestCase):

    def setUp(self):
        self._deck = Deck(range(100))
        self._deck.shuffle()


    def test_refill(self):
        pulled = set()
        for _ in range(10):
            pulled.add(self._deck.take_top())

        for card in pulled:
            self._deck.discard(card)

        self._deck.refill()

        repulled = set()
        for _ in range(10):
            repulled.add(self._deck.take_top())

        self.assertEqual(len(pulled.intersection(repulled)), len(pulled))

    def test_isEmpty(self):
        pulled = set()
        for _ in range(self._deck.remaining()):
            self.assertFalse(self._deck.is_empty())
            pulled.add(self._deck.take_top())

        self.assertTrue(self._deck.is_empty())

        for card in pulled:
            self._deck.discard(card)

        self.assertTrue(self._deck.is_empty())

        self._deck.refill()

        self.assertFalse(self._deck.is_empty())

    def test_take_bottom(self):
        pulled = set()
        for _ in range(10):
            pulled.add(self._deck.take_top())

        for card in pulled:
            self._deck.discard(card)

        self._deck.refill()

        bottom_pulled = set()
        for _ in range(10):
            bottom_pulled.add(self._deck.take_bottom())

        repulled = set()
        for _ in range(10):
            repulled.add(self._deck.take_top())

        self.assertEqual(len(pulled.intersection(repulled)), len(pulled))
        self.assertEqual(len(pulled.intersection(bottom_pulled)), 0)

    def test_shuffle(self):

        clone = Deck(set())
        clone._deck = self._deck._deck.copy()
        clone.shuffle()

        pulled = []
        for _ in range(self._deck.remaining()):
            pulled.append(self._deck.take_top())

        clone_pulled = []
        for _ in range(clone.remaining()):
            clone_pulled.append(clone.take_top())

        self.assertEqual(len(pulled), len(clone_pulled))
        equal = True
        for i in range(len(pulled)):
            equal = equal and (pulled[i] == clone_pulled[i])
            if not equal:
                break
        self.assertFalse(equal)

        self.assertEqual(len(set(pulled).intersection(set(clone_pulled))), len(pulled))
