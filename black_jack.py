from deck import Deck
from player import Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()

    def play(self):
        user = Player()
        # przemyśleć poniższą kwestię
        for _ in range(2):
            card = self.deck.give_a_card()
            user.take_card(card)

        print(user.cards)
        print(user.calculate_points())



