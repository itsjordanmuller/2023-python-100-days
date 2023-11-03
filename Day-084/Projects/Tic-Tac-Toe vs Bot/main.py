import random
import time


class TicTacToeCLI:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.players = {"Player": "", "Bot": ""}
        self.current_turn = ""
        self.game_over = False
        self.scores = {"Player": 0, "Bot": 0}
        self.round = 1

        marks = ["X", "O"]
        random.shuffle(marks)
        self.players["Player"], self.players["Bot"] = marks

        self.current_turn = (
            "Player" if random.choice(marks) == self.players["Player"] else "Bot"
        )

    def print_board(self):
        top_border = f"/-----------\\"
        bottom_border = f"\\-----------/"
        internal_border = "|---+---+---|"

        print("\n Positions Key:\t\tCurrent Board:")
        for i in range(3):
            key_row = ""
            game_row = ""
            for j in range(3):
                key_row += "| " + str(i * 3 + j + 1) + " "
                game_row += (
                    "| "
                    + (self.board[i * 3 + j] if self.board[i * 3 + j] != " " else " ")
                    + " "
                )
            key_row += "|"
            game_row += "|"

            if i == 0:
                print(top_border + "\t\t" + top_border)
            print(key_row + "\t\t" + game_row)
            if i == 2:
                print(bottom_border + "\t\t" + bottom_border)
            else:
                print(internal_border + "\t\t" + internal_border)

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

    def bot_move(self):
        print("\nBot is thinking...", end="", flush=True)
        time.sleep(random.randint(0, 2))
        print("\r", end="")
        available_positions = [i for i, spot in enumerate(self.board) if spot == " "]
        position = random.choice(available_positions)
        self.place_mark(position)

    def place_mark(self, position):
        mark = self.players[self.current_turn]
        self.board[position] = mark
        if self.check_win(mark):
            print(f"{self.current_turn} wins!")
            self.scores[self.current_turn] += 1
            self.game_over = True
        elif self.check_draw():
            print("It's a draw!")
            self.game_over = True
        self.current_turn = "Bot" if self.current_turn == "Player" else "Player"

    def play_round(self):
        self.reset_board()
        while not self.game_over:
            self.print_board()
            if self.current_turn == "Player":
                try:
                    position = (
                        int(
                            input(
                                f"\nPlayer ({self.players['Player']}), enter your move (1-9): "
                            )
                        )
                        - 1
                    )
                    if 0 <= position <= 8 and self.board[position] == " ":
                        self.place_mark(position)
                    else:
                        print("Invalid move. Choose a number from 1 to 9.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("\nBot is making a move...")
                self.bot_move()

    def play_game(self):
        while True:
            print(f"\nRound {self.round}")
            print(
                f"Scores: Player ({self.players['Player']}) - {self.scores['Player']}, Bot ({self.players['Bot']}) - {self.scores['Bot']}"
            )
            self.play_round()
            play_again = input("Do you want to play another round? (y/n): ").lower()
            if play_again == "y":
                self.round += 1
                self.current_turn = (
                    "Player"
                    if random.choice(["X", "O"]) == self.players["Player"]
                    else "Bot"
                )
                continue
            else:
                print("Final Scores:")
                print(f"Player ({self.players['Player']}): {self.scores['Player']}")
                print(f"Bot ({self.players['Bot']}): {self.scores['Bot']}")
                print("Thanks for playing!")
                break


if __name__ == "__main__":
    game = TicTacToeCLI()
    game.play_game()
