from game.black_jack import Game
from tests.exceptions import GameOverCroupierException,GameOverUserException, GameOverDrawException

try:
    game = Game()
    game.play()

# except GameOverException:
#     print(f'Player game over user exception')

except GameOverCroupierException:
    print("Player wins!")

except GameOverUserException:
    print(f"Croupier wins!")





#
# if __name__ == '__main__':
# #     pass

# Krupier pobiera kartę przy 'pass" czyli wyborze '2', nie moze tego robić, więc musi bazowac tylkoa
# na rozdanych kartach
# WARUNEK WHILE JEST BŁĘDNY ZE TAK ROBI i KONIEC KROPKA - ZMIENIC