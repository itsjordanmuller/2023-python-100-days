import random


class TicTacToeCLI:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_turn = "X"
        self.game_over = False
        self.x_score = 0
        self.o_score = 0
        self.round = 1
