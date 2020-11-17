import unittest

from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Hearts", 6)


    def test_checkForAce__true(self):
        check_result = CardGame.checkforAce(self, self.card1)
        self.assertEqual(True, check_result)


    def test_checkForAce__false(self):
        check_result = CardGame.checkforAce(self, self.card2)
        self.assertEqual(False, check_result)

    
    def test_checkHighestCard__card2_higher(self):
        check_result = CardGame.highest_card(self, self.card1, self.card2)
        self.assertEqual(self.card2, check_result)

    
    def test_checkHighestCard__card3_higher(self):
        card3 = Card("Spades", 10)
        check_result = CardGame.highest_card(self, self.card3, self.card2)
        self.assertEqual(self.card3, check_result)

    
    def test_cards_total(self):
        self.assertEqual("You have a total of 7", CardGame.cards_total())