"""
Module where all mechanics is implemented
"""

from tests.exceptions import GameOverException, GameOverUserException, GameOverCroupierException
from game.deck import Deck
from game.player import Player


class Game:
    """
    Class that represents mechanics of the game and gather all information
    """

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        self.choice = None
        self.croupier = Player()
        self.user = Player()

    @staticmethod
    def _menu():

        """
        The _menu function prints out the menu options for the user to choose from.
            It takes no arguments and returns nothing.

        :return: The user's choice
        :doc-author: Trelent
        """
        print("What would you like to do?:")
        print("1 - take a card ")
        print("2 - pass")

    def _croupier_plays(self, user_points):

        """
        The _croupier_plays function is a helper function that allows the croupier to play.
        It takes in user_points as an argument and returns the croupier's points.
        The function first gives a card to the croupier,
        then while his points are less than
        the user's points, it will give him another card
        until he has more or equal amount of points as the user.

        :param self: Represent the instance of the object itself
        :param user_points: Determine when the croupier should stop taking cards
        :return: The croupier's points
        :doc-author: Trelent
        """
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

        """
        The _user_plays function is a method of the Game class.
        It takes no arguments and returns an integer value representing
        the total points accumulated by the user during their turn.
        The function begins by creating a Player object called 'user'
        and then deals two cards to that player from the deck using take_card().
        A while loop is used to allow for repeated
        interactions with the user until they choose to stop taking cards
        or go over 21 points, at which point they lose and
        the game ends. The _menu() method prints out options for
        what action can be taken on each turn, and input() allows them to make

        :param self: Access the attributes and methods of the class in python
        :return: The user's points
        :doc-author: Trelent
        """
        user = Player()
        for _ in range(2):
            card = self.deck.give_a_card()
            user.take_card(card)

        while True:
            print("---" * 5)
            print("Player:", user.cards)
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

        """
        The play function is the main function of the game.
        It calls two other functions, _user_plays and _croupier_plays.
        The first one asks for user input to play a card from his hand,
        while the second one plays a card from croupier's hand.
        If either player has no cards left in their hands, they lose.

        :param self: Access the attributes and methods of a class
        :return: A string
        :doc-author: Trelent
        """
        try:
            user_points = self._user_plays()
        except GameOverException as error:
            raise GameOverUserException from error

        try:
            self._croupier_plays(user_points)

        except GameOverException as error:
            raise GameOverCroupierException from error

        print("End of game. Croupier wins!")
