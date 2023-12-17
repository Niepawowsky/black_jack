from card import Card


class Player:
    def __init__(self):
        self.cards = []
        # self.score = 0

    def take_card(self, card:Card):
        self.cards.append(card)

    def calculate_points(self):
        points = 0
        number_of_aces = len([card for card in self.cards if card.figure == 'Ace'])

        if number_of_aces == 2 and len(self.cards) == 2:
            return 21

        if number_of_aces == 1 and len(self.cards) == 2:
            points = 10

        for card in self.cards:
            if card.figure == 'Ace':
                points += 1
            elif card.figure in ['Jack', 'Queen', 'King']:
                points += 10
            else:
                points += card.figure

        return points