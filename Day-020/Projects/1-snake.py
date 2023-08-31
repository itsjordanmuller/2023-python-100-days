from turtle import Turtle, Screen
import time


def create_segment(x, y):
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(x, y)
    return segment


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

segments = []
for i in range(3):
    x_position = i * -20
    segment = create_segment(x_position, 0)
    segments.append(segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)

screen.exitonclick()
