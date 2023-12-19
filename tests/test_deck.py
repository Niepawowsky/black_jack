"""
Tests for deck module
"""
from game.deck import Deck


def test_deck_cards_amount():
    """
    The test_deck_cards_amount function tests the Deck class
    to ensure that it has 52 cards.


    :return: The number of cards in the deck
    :doc-author: Trelent
    """
    deck = Deck()

    assert len(repr(deck)) == 52


def test_shuffle_deck():
    """
    The test_shuffle_deck function tests the shuffle_deck function in
    the Deck class.
    It creates two decks, one that is shuffeled and one that is not.
    It then compares them to see if they are equal.

    :return: True if the shuffeled deck is not equal to the original deck
    :doc-author: Trelent
    """
    deck = Deck()
    shuffeled_deck = Deck()

    shuffeled_deck.shuffle_deck()

    assert not deck == shuffeled_deck


def test_take_a_card():
    """
    The test_take_a_card function tests the give_a_card function in the Deck class.
    It creates a deck, then gives two cards from it.
    It then checks that there are 50 cards left in the deck.

    :return: The number of cards left in the deck
    :doc-author: Trelent
    """
    deck = Deck()
    deck.give_a_card()
    deck.give_a_card()
    assert len(repr(deck)) == 50
