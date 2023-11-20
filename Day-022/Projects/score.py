from turtle import Turtle

# Scoreboard text settings
ALIGNMENT = "center"
FONT = ("Courier", 32, "normal")
BIG_FONT = ("Courier", 48, "normal")


class Scoreboard(Turtle):
    """
    Represents the scoreboard in the Pong game.
    Tracks and displays scores, and handles end-game scenarios.
    """

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()
        self.game_is_over = False

    def update_score(self):
        # Clear and display current scores
        self.clear()
        self.display_left_score()
        self.display_right_score()

    def display_left_score(self):
        # Display the left player's score
        self.goto(-200, 180)
        self.write(self.left_score, align=ALIGNMENT, font=BIG_FONT)

    def display_right_score(self):
        # Display the right player's score
        self.goto(200, 180)
        self.write(self.right_score, align=ALIGNMENT, font=BIG_FONT)

    def increase_left_score(self):
        # Increment left player's score and check for game end
        self.left_score += 1
        self.update_score()
        if self.left_score == 5:
            self.game_over("Left Player")

    def increase_right_score(self):
        # Increment right player's score and check for game end
        self.right_score += 1
        self.update_score()
        if self.right_score == 5:
            self.game_over("Right Player")

    def game_over(self, winner):
        # Handle end of the game scenario
        self.game_is_over = True
        self.display_game_over_message(winner)

    def display_game_over_message(self, winner):
        # Display 'Game Over' message and the winner
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=BIG_FONT)
        self.goto(0, -50)
        self.write(f"{winner} Wins!", align=ALIGNMENT, font=FONT)
