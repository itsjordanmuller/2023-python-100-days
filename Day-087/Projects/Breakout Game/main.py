import time
from turtle import Screen
from paddle import Paddle
from bricks import create_bricks, BRICK_CONFIGS

screen = Screen()
screen.setup(width=500, height=800)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -330))

brick_size = "medium"
bricks = create_bricks(BRICK_CONFIGS[brick_size])

screen.listen()
screen.onkey(fun=paddle.move_left, key="Left")
screen.onkey(fun=paddle.move_right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)

screen.exitonclick()
