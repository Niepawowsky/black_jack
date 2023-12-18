from black_jack import Game
from exceptions import GameOverCroupierException,GameOverUserException

try:
    game = Game()
    game.play()
except GameOverCroupierException:
    print("Player wins!")
except GameOverUserException:
    print("Croupier wins! ")

#
# if __name__ == '__main__':
# #     pass
