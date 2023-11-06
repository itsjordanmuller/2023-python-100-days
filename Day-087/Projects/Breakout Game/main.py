import time
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=500, height=900)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -400))

screen.listen()
screen.onkey(fun=paddle.move_left, key="Left")
screen.onkey(fun=paddle.move_right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)

screen.exitonclick()
