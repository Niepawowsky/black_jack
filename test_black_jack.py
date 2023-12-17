from black_jack import Game

def test_cards_on_player_hand():
    game = Game()
    cards = game.play()



    assert len(cards) == 2


