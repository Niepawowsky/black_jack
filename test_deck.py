from deck import Deck
from card import Card

def test_deck_cards_amount():
    deck = Deck()

    assert len(deck.__repr__()) == 52

def test_shuffle_deck():
    deck = Deck()
    shuffeled_deck = Deck()

    shuffeled_deck.shuffle_deck()

    assert deck != shuffeled_deck

def test_take_a_card():
    deck = Deck()
    deck.take_a_card(2)

    assert deck == 50