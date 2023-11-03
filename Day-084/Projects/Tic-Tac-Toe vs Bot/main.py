import random


class TicTacToeCLI:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_turn = "X"
        self.game_over = False
        self.x_score = 0
        self.o_score = 0
        self.round = 1

    def print_board(self):
        for i in range(3):
            row = ""
            for j in range(3):
                if self.board[i * 3 + j] == " ":
                    row += str(i * 3 + j + 1)
                else:
                    row += self.board[i * 3 + j]
                if j < 2:
                    row += " | "
            print(row)
            if i < 2:
                print("---------")
