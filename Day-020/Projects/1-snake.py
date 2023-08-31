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

direction = "right"


def move_left():
    global direction
    if direction != "right":
        direction = "left"


def move_right():
    global direction
    if direction != "left":
        direction = "right"


def move_up():
    global direction
    if direction != "down":
        direction = "up"


def move_down():
    global direction
    if direction != "up":
        direction = "down"


screen.listen()
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        x = segments[seg_num - 1].xcor()
        y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(x, y)

    if direction == "up":
        segments[0].setheading(90)
    elif direction == "down":
        segments[0].setheading(270)
    elif direction == "left":
        segments[0].setheading(180)
    elif direction == "right":
        segments[0].setheading(0)

    segments[0].forward(20)

screen.exitonclick()
