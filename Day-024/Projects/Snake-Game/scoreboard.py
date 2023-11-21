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
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.get_high_score()
        self.update_score()

    def get_high_score(self):
        """Update and display the current score."""
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
            print(self.high_score)

    def update_score(self):
        """Update scores"""
        self.clear()
        self.write(
            f"Score: {self.score} | High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        """Increase the score by 1."""
        self.score += 1
        self.update_score()

    def reset(self):
        """Reset the game and show the new high score."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
