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

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.clear()
        self.game_is_over = True
        self.goto(0, 25)
        self.color("black")
        self.write("GAME OVER", align="center", font=FONT)
        self.goto(0, -25)
        self.write(f"You made it to Level {self.level}", align="center", font=FONT)
