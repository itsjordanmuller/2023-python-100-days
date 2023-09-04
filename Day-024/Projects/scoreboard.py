from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
BIG_FONT = ("Courier", 32, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 10)
    #     self.color("red")
    #     self.write(f"GAME OVER!", align=ALIGNMENT, font=BIG_FONT)
    #     self.goto(0, -30)
    #     self.write(f"Final Score: {self.score}", align=ALIGNMENT, font=FONT)
