from turtle import Turtle
import math
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed = 10
        self.angle = random.randint(225, 315)
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.speed * math.cos(math.radians(self.angle))
        new_y = self.ycor() + self.speed * math.sin(math.radians(self.angle))
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.angle = 360 - self.angle

    def bounce_x(self):
        self.angle = 180 - self.angle

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.05
        self.angle = 135

    def set_angle(self, angle):
        self.angle = angle
