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

    def move(self):
        self.forward(10)
