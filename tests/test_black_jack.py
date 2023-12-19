"""
Tests for blackjack module
"""
from game.black_jack import Game


def test_cards_on_player_hand():
    """
    The test_cards_on_player_hand function tests that the player has two cards on their hand.


    :return: A list of 2 cards
    :doc-author: Trelent
    """
    game = Game()
    cards = game.play()

    assert len(cards) == 2
