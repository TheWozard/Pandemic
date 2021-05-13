import unittest

from game.cards.player_deck import create_player_deck
from game.params import Cities, CitiesInPlay, SpecialCards

cities = [
    Cities.SanFrancisco, Cities.Chicago, Cities.Montreal, Cities.NewYork, Cities.Atlanta, Cities.Washington, Cities.London, Cities.Essen, Cities.StPetersburg, Cities.Madrid, Cities.Paris, Cities.Milan,
]

class TestDeckMethods(unittest.TestCase):

    def test_create(self):
        for _ in range(100):
            deck = create_player_deck(cities, 1, 2, 4)
            self.assertEqual(deck.remaining(), 14)

            for _ in range(4):
                self.assertFalse(deck.take_top() == SpecialCards.Infection)

            found = 0
            for _ in range(5):
                if deck.take_top() == SpecialCards.Infection:
                    found += 1
            
            self.assertEqual(found, 1)

            for _ in range(5):
                if deck.take_top() == SpecialCards.Infection:
                    found += 1

            self.assertEqual(found, 2)
            self.assertTrue(deck.is_empty())
