import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Hearts", 6)

    def test_checkforAce__true(self):
        check_result = CardGame.checkforAce(self, self.card1)
        self.assertEqual(True, check_result)

    def test_checkforAce__false(self):
        check_result = CardGame.checkforAce(self, self.card2)
        self.assertEqual(False, check_result)