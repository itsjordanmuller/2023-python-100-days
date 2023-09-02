from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=858, height=525)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((410, 0))
left_paddle = Paddle((-415, 0))

ball = Ball()

screen.listen()
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")
screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")

game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(0.05)

screen.exitonclick()
