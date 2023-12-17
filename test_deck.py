from deck import Deck
from card import Card

def test_deck_cards_amount():
    deck = Deck()

    assert len(deck.__repr__()) == 52

def test_shuffle_deck():
    deck = Deck()
    shuffeled_deck = Deck()

    shuffeled_deck.shuffle_deck()

    assert not deck == shuffeled_deck

def test_take_a_card():
    deck = Deck()
    deck.give_a_card()
    deck.give_a_card()
    assert len(deck.__repr__()) == 50