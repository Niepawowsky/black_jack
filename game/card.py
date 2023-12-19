class InvalidCardColor(Exception):
    pass


class InvalidCardFigure(Exception):
    pass


class Card:
    possible_color = {"clubs": chr(9827),
                      "diamonds": chr(9830),
                      "hearts": chr(9829),
                      "spades": chr(9824)}

    possible_figure = (list(range(2, 11))
                       + ['Jack', 'Queen', 'King', 'Ace'])

    def __init__(self, color, figure):
        if color not in self.possible_color:
            raise InvalidCardColor("You picked wrong color")
        self.color = self.possible_color[color]
        if figure not in self.possible_figure:
            raise InvalidCardFigure("You picked wrong figure")
        self.figure = figure

    def __repr__(self):
        return f'{self.figure} - {self.color}'

    # def card_generator(self):

    #
    #
    # def pass_cards(self):
    #     cards = self._create_card()
    #     return cards
