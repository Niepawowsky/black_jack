import pytest

from game.card import Card, InvalidCardColor, InvalidCardFigure


def test_card_creator():
    card1 = Card('diamonds', 2)
    card2 = Card('hearts', "Ace")

    assert card1.figure == 2
    assert card1.color == chr(9830)
    assert card2.figure == "Ace"
    assert card2.color == chr(9829)


def test_create_wrong_figure():
    with pytest.raises(InvalidCardFigure) as m:
        card1 = Card('spades', "Q")
        assert m == "You picked wrong figure"


def test_create_wrong_color():
    with pytest.raises(InvalidCardColor) as m:
        card1 = Card('yellow', "Q")
        assert m == "You picked wrong color"


def test_card_repr():
    assert repr(Card('hearts', "Queen") == f'Queen - {chr(9827)}')
    assert repr(Card('spades', "King") == f'Queen - {chr(9827)}')
    assert repr(Card('diamonds', "Queen") == f'Queen - {chr(9827)}')
    assert repr(Card('clubs', "Queen") == f'Queen - {chr(9827)}')
