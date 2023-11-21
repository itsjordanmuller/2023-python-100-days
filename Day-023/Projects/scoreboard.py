from turtle import Turtle

# Font configuration for scoreboard
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_level()

    # Update and display the current level
    def update_level(self):
        self.clear()
        self.goto(-285, 255)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    # Increase level and update display
    def increase_level(self):
        self.level += 1
        self.update_level()

    # Display game over message and final level
    def game_over(self):
        self.clear()
        self.goto(0, 25)
        self.write("GAME OVER", align="center", font=FONT)
        self.goto(0, -25)
        self.write(f"You made it to Level {self.level}", align="center", font=FONT)
