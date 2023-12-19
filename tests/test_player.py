from game.player import Player
from game.card import Card


def test_calculate_player_points():
    card1 = Card('hearts', 3)
    card2 = Card('diamonds', 5)
    player = Player()

    player.take_card(card1)
    player.take_card(card2)

    assert player.calculate_points() == 8


def test_calculate_player_points_double_aces():
    card1 = Card('hearts', 'Ace')
    card2 = Card('diamonds', 'Ace')
    player = Player()

    player.take_card(card1)
    player.take_card(card2)

    assert player.calculate_points() == 21


def test_calculate_player_points_triple_ace():
    card1 = Card('hearts', 'Ace')
    card2 = Card('diamonds', 'Ace')
    card3 = Card('spades', 'Ace')
    player = Player()

    player.take_card(card1)
    player.take_card(card2)
    player.take_card(card3)

    assert player.calculate_points() == 3


def test_calculate_player_points_one_ace_two_cards():
    card1 = Card('hearts', 'Ace')
    card2 = Card('diamonds', 5)
    player = Player()

    player.take_card(card1)
    player.take_card(card2)

    assert player.calculate_points() == 16

def test_calculate_player_points_one_ace_other_no_number():
    card1 = Card('hearts', 'Ace')
    card2 = Card('diamonds', 'King')
    player = Player()

    player.take_card(card1)
    player.take_card(card2)

    assert player.calculate_points() == 21