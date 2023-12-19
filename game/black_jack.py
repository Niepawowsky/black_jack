from game.deck import Deck
from tests.exceptions import GameOverException, GameOverUserException, GameOverCroupierException, GameOverDrawException
from game.player import Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.choice = None
        self.croupier = Player()
        self.user = Player()


    @staticmethod
    def _menu():
        print("What would you like to do?:")
        print("1 - take a card ")
        print("2 - pass")


    def _croupier_plays(self, user_points):
        card = self.deck.give_a_card()
        self.croupier.take_card(card)
        while self.croupier.calculate_points() < user_points:
            self.croupier.take_card(self.deck.give_a_card())
            print("---" * 5)
            print("Croupier:")
            print(self.croupier.cards)
            print(self.croupier.calculate_points())
            print("---" * 5)

        return self.croupier.calculate_points()



    def _user_plays(self):
        user = Player()
        for _ in range(2):
            card = self.deck.give_a_card()
            user.take_card(card)

        while True:
            print("---" * 5)
            print("Player:" ,user.cards)
            print(f'Points: {user.calculate_points()}')
            print("---" * 5)
            self._menu()
            self.choice = input('Choose 1 or 2: ')
            if self.choice == "1":
                user.take_card(self.deck.give_a_card())
            elif self.choice == '2':
                return user.calculate_points()
            else:
                print('Wrong choice!')

    def play(self):

        try:
            user_points = self._user_plays()
        except GameOverException as error:
            raise GameOverUserException from error


        try:
            croupier_points = self._croupier_plays(user_points)

        except GameOverException as error:
            raise GameOverCroupierException from error


        print("End of game. Croupier wins!")






    # def print_croupier_points(self):
    #     points = self._croupier_plays()
    #     return points
    #
    #

