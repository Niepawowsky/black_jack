"""
This module contains class Player which represents persons who play in real game:
player and croupier
"""
from tests.exceptions import GameOverException
from game.card import Card


class Player:
    """
    Class that creates player - either croupier (computer) or user (human)
    """

    def __init__(self):
        self.cards = []
        self.score = 0

    def __eq__(self, other):
        return self.score == other.score

    def take_card(self, card: Card):

        """
        The take_card function takes a card object as an argument
         and appends it to the player's hand.

        :param self: Represent the instance of the class
        :param card:Card: Specify the type of object that is being passed into the function
        :return: The card that was taken
        :doc-author: Trelent
        """
        self.cards.append(card)

    def calculate_points(self):

        """
        The calculate_points function takes the cards in a hand and returns the total points.

        :param self: Refer to the object itself
        :return: The total points of the cards in the hand
        :doc-author: Trelent
        """
        points = 0
        number_of_aces = len([card for card in self.cards if card.figure == 'Ace'])

        if number_of_aces == 2 and len(self.cards) == 2:
            return 21

        if number_of_aces == 1 and len(self.cards) == 2:
            points = 10

        for card in self.cards:
            if card.figure == 'Ace':
                points += 1
            elif card.figure in ['Jack', 'Queen', 'King']:
                points += 10
            else:
                points += card.figure

        if points > 21:
            raise GameOverException

        return points
