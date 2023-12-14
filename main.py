
from card import Card


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class Dealer(Player):
    def __init__(self, name):
        super.__init__(name)


class Human(Player):
    def __init__(self, name):
        super.__init__(name)

    def create_player(self):
        nick = input('Give me your nick')
        return nick







card = Card
print(card._create_card)

if __name__ == '__main__':
    pass
