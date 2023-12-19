"""
This module contains class Card which represents one unit of card

"""


class InvalidCardColor(Exception):
    """
    Class that represents invalid card color
    """


class InvalidCardFigure(Exception):
    """
        Class that represents invalid card figure
    """


class Card:
    """
    Class that holds one, unique type of card. Before it
    it creates it.
    """
    possible_color = {"clubs": chr(9827),
                      "diamonds": chr(9830),
                      "hearts": chr(9829),
                      "spades": chr(9824)}

    possible_figure = (list(range(2, 11))
                       + ['Jack', 'Queen', 'King', 'Ace'])

    def __init__(self, color, figure):

        """
        The __init__ function is the constructor of a class.
        It is called when an object of this class
        is created and it allows to initialize the attributes of
        this object.

        :param self: Represent the instance of the object itself
        :param color: Set the color of the card
        :param figure: Define the card's figure
        :return: The object itself
        :doc-author: Trelent
        """
        if color not in self.possible_color:
            raise InvalidCardColor("You picked wrong color")
        self.color = self.possible_color[color]
        if figure not in self.possible_figure:
            raise InvalidCardFigure("You picked wrong figure")
        self.figure = figure

    def __repr__(self):
        return f'{self.figure} - {self.color}'
