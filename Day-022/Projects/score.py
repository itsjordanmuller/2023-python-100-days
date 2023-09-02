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
        self.game_is_over = False

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

    def increase_left_score(self):
        self.left_score += 1
        self.update_score()
        if self.left_score == 5:
            self.game_over("Left Player")

    def increase_right_score(self):
        self.right_score += 1
        self.update_score()
        if self.right_score == 5:
            self.game_over("Right Player")

    def game_over(self, winner):
        self.game_is_over = True
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER!", align=ALIGNMENT, font=BIG_FONT)
        self.goto(0, -50)
        self.write(f"{winner} Wins!", align=ALIGNMENT, font=FONT)
