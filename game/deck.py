"""
Module that is responsible for creating deck from provided cards
"""

from random import shuffle
from game.card import Card


class Deck:
    """
    Class that creates list of deck from provided cards
    """

    def __init__(self):

        """
        The __init__ function is called when the class is instantiated.
        It sets up the deck with all possible cards, and shuffles it.

        :param self: Refer to the current instance of a class
        :return: The deck
        :doc-author: Trelent
        """
        self.deck = []
        for color in Card.possible_color:
            for figure in Card.possible_figure:
                self.deck.append(
                    Card(color=color, figure=figure)
                )

    def __repr__(self):
        return self.deck

    def __eq__(self, other):
        self.deck == other.deck

    def shuffle_deck(self) -> None:

        """
        The shuffle_deck function shuffles the deck of cards.


        :param self: Refer to the object itself
        :return: None
        :doc-author: Trelent
        """
        shuffle(self.deck)

    def give_a_card(self):

        """
        The give_a_card function takes a card from the deck and returns it to the player.


        :param self: Refer to the object that is calling the function
        :return: A card from the deck
        :doc-author: Trelent
        """
        card = self.deck.pop()
        return card
