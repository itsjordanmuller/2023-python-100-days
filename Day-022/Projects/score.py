from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 32, "normal")
BIG_FONT = ("Courier", 48, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.display_left_score()
        self.display_right_score()

    def display_left_score(self):
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)

    def display_right_score(self):
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)
