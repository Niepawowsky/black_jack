"""
Tests for card module
"""

import pytest

from game.card import Card, InvalidCardColor, InvalidCardFigure


def test_card_creator():
    """
    The test_card_creator function tests the Card class.
    It creates two cards and checks if their attributes are correct.

    :return: The correct figure and color for the cards
    :doc-author: Trelent
    """
    card1 = Card('diamonds', 2)
    card2 = Card('hearts', "Ace")

    assert card1.figure == 2
    assert card1.color == chr(9830)
    assert card2.figure == "Ace"
    assert card2.color == chr(9829)


def test_create_wrong_figure():
    """
    The test_create_wrong_figure function tests if the user picks a wrong figure.
        If so, it raises an InvalidCardFigure exception.

    :return: An error message when a wrong figure is picked
    :doc-author: Trelent
    """
    with pytest.raises(InvalidCardFigure) as m:
        card1 = Card('spades', "Q")
        assert m == "You picked wrong figure"


def test_create_wrong_color():
    """
    The test_create_wrong_color function tests the Card class to see if it can handle an invalid color.
        The test_create_wrong_color function creates a card with an invalid color and then checks to see if the
        InvalidCardColor exception is raised.

    :return: A message that the color is invalid
    :doc-author: Trelent
    """
    with pytest.raises(InvalidCardColor) as m:
        card1 = Card('yellow', "Q")
        assert m == "You picked wrong color"


def test_card_repr():
    """
    The test_card_repr function tests the repr method of the Card class.
        It checks that each suit is represented by its unicode character and that
        each card value is represented by its string name.

    :return: The card's rank and suit
    :doc-author: Trelent
    """
    assert repr(Card('hearts', "Queen") == f'Queen - {chr(9827)}')
    assert repr(Card('spades', "King") == f'Queen - {chr(9827)}')
    assert repr(Card('diamonds', "Queen") == f'Queen - {chr(9827)}')
    assert repr(Card('clubs', "Queen") == f'Queen - {chr(9827)}')
