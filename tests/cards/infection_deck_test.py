import unittest

from game.cards.infection_deck import create_infection_deck
from game.params import Cities


class TestDeckMethods(unittest.TestCase):

    def test_create(self):
        deck = create_infection_deck([Cities.SanFrancisco, Cities.Chicago], 2)
        self.assertEqual(deck.remaining(), 4)
