from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.length = 3
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=self.length)
        self.penup()
        self.goto(position)

    def move_left(self):
        if self.xcor() - (self.length * 10) > -240:
            move_x = self.xcor() - 25
            self.goto(move_x, self.ycor())

    def move_right(self):
        if self.xcor() + (self.length * 10) < 240:
            move_x = self.xcor() + 25
            self.goto(move_x, self.ycor())
