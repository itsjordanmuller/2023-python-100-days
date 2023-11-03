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

    def check_win(self, mark):
        win_conditions = [
            # rows
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            # columns
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            # diagonals
            [0, 4, 8],
            [2, 4, 6],
        ]
        for condition in win_conditions:
            if all(self.board[i] == mark for i in condition):
                return True
        return False

    def check_draw(self):
        return " " not in self.board

    def place_mark(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_turn
            if self.check_win(self.current_turn):
                print(f"{self.current_turn} wins!")
                if self.current_turn == "X":
                    self.x_score += 1
                else:
                    self.o_score += 1
                self.game_over = True
            elif self.check_draw():
                print("It's a draw!")
                self.game_over = True
            self.current_turn = "O" if self.current_turn == "X" else "X"
        else:
            print("Position already taken. Choose another one.")

    def reset_board(self):
        self.board = [" " for _ in range(9)]
        self.game_over = False
