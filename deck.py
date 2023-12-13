from card import Card
from random import shuffle


class Deck:
    def __init__(self):
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
        return shuffle(self.deck)

    def take_a_card(self, number_taken: int):
        counter = 0

        while counter != number_taken:
            self.deck.pop(-1)

    # def _deck_generator(self):
    #     for color in self.card.possible_color:
    #         for figure in self.card.possible_figure:
    #             self.card = Card(color, figure)
    #             self.deck.append(self.card)
    #     return self.deck
deck = Deck()

print(deck.__repr__())