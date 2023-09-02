from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self):
        move_y = self.ycor() + 20
        self.goto(self.xcor(), move_y)

    def move_down(self):
        move_y = self.ycor() - 20
        self.goto(self.xcor(), move_y)
