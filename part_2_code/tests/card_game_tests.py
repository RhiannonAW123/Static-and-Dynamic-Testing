import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cardgame = CardGame ()
        self.card1 = Card("Spades", 2)
        self.card2 = Card("Hearts", 6)
        self.card3 = Card("Clubs", 9)
        self.cards = [self.card1, self.card2, self.card3]

    def test_check_for_ace(self):
        self.assertEqual(False, self.cardgame.check_for_ace(self.card1))  


    def test_highest_card(self):
        self.assertEqual(self.card2, self.cardgame.highest_card(self.card1, self.card2))
        self.assertEqual(self.card3, self.cardgame.highest_card(self.card3, self.card2))
        self.assertEqual(self.card3, self.cardgame.highest_card(self.card1, self.card3))

    def test_cards_total(self):
        self.assertEqual("You have a total of 17", self.cardgame.cards_total(self.cards))
