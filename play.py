import sys


def start(player1_type, player2_type):
    
    import state as s
    import player as p
    import driver as game
    state = s.GameState()
    player1 = p.Player(1, player1_type)
    player2 = p.Player(2, player2_type)
    begin = game.driver()
    begin.startplay(state, player1, player2)


if __name__ == "__main__":
    player1_type = int(sys.argv[1])
    player2_type = int(sys.argv[2])
    start(player1_type, player2_type)