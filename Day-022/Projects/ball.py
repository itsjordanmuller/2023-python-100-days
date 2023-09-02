from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.penup()
        self.angle = random.choice([random.randint(-25, 25), random.randint(155, 205)])
        self.setheading(self.angle)

    def move(self, right_paddle, left_paddle):
        self.forward(10)

        if (
            self.xcor() > right_paddle.xcor() - 10
            and self.xcor() < right_paddle.xcor() + 10
            and self.ycor() < right_paddle.ycor() + 90
            and self.ycor() > right_paddle.ycor() - 90
        ):
            self.bounce()

        if (
            self.xcor() < left_paddle.xcor() + 10
            and self.xcor() > left_paddle.xcor() - 10
            and self.ycor() < left_paddle.ycor() + 90
            and self.ycor() > left_paddle.ycor() - 90
        ):
            self.bounce()

    def bounce(self):
        current_angle = self.heading()
        new_angle = 180 - current_angle
        self.setheading(new_angle)
