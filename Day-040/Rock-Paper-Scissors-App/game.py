import random


class Game:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.choices = ["rock", "paper", "scissors"]

    def player_move(self, choice):
        computer_choice = self.computer_move()
        return self.calculate_result(choice, computer_choice)

    def computer_move(self):
        return random.choice(self.choices)

    def calculate_result(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "draw", player_choice, computer_choice
        elif (
            (player_choice == "rock" and computer_choice == "scissors")
            or (player_choice == "scissors" and computer_choice == "paper")
            or (player_choice == "paper" and computer_choice == "rock")
        ):
            self.player_score += 1
            return "player", player_choice, computer_choice
        else:
            self.computer_score += 1
            return "computer", player_choice, computer_choice

    def get_scores(self):
        return self.player_score, self.computer_score

    def reset(self):
        self.player_score = 0
        self.computer_score = 0
