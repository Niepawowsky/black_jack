"""
Module to run the game
"""

from game.black_jack import Game
from tests.exceptions import GameOverCroupierException, GameOverUserException

try:
    game = Game()
    game.play()


except GameOverCroupierException:
    print("Player wins!")

except GameOverUserException:
    print("Croupier wins!")
