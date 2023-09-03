from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-285, 255)
        self.write(f"Level: {self.level}", align="left", font=FONT)
