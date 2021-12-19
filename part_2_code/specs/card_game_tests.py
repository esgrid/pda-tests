import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def test_check_for_ace(self):
        juego = CardGame()
        card = Card("hearts", 1)
        self.assertEqual(True, juego.check_for_ace(card))

    def test_highest_card(self):
        card1 = Card("hearts", 6)
        card2 = Card("spades", 4)
        juego = CardGame()
        self.assertEqual(card1.value, juego.highest_card(card1, card2).value)

    def test_card_total(self):
        cards = [Card("spades", 1), Card("hearts", 5), Card("diamonds", 5), Card("clubs", 8)]
        juego = CardGame()
        self.assertEqual("You have a total of 19", juego.cards_total(cards))