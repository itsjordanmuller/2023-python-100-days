from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
BIG_FONT = ("Courier", 32, "normal")


class Scoreboard(Turtle):
    """Creates and handles scoreboard in the Snake game."""

    def __init__(self):
        """Initialize the scoreboard with default properties."""
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.update_score()

    def update_score(self):
        """Update and display the current score."""
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score by 1."""
        self.score += 1
        self.update_score()

    def game_over(self):
        """Display the game over message and the final score."""
        self.goto(0, 10)
        self.color("red")
        self.write(f"GAME OVER!", align=ALIGNMENT, font=BIG_FONT)
        self.goto(0, -30)
        self.write(f"Final Score: {self.score}", align=ALIGNMENT, font=FONT)
