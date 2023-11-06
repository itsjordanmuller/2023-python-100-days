import time
import random
from turtle import Screen

from ball import Ball
from bricks import BRICK_CONFIGS, create_bricks
from paddle import Paddle

screen = Screen()
screen.setup(width=500, height=800)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -330))

brick_size = random.choice(["small", "medium", "large"])
bricks = create_bricks(BRICK_CONFIGS[brick_size])

ball = Ball()


def check_collision_with_walls():
    if ball.ycor() > 380:
        ball.bounce_y()

    if ball.xcor() > 240 or ball.xcor() < -240:
        ball.bounce_x()


def check_collision_with_paddle():
    if ball.distance(paddle) < 50 and ball.ycor() < -300:
        ball.bounce_y()


def check_collision_with_bricks():
    for brick in bricks[:]:
        if ball.distance(brick) < 20:
            brick.destroy()
            bricks.remove(brick)
            ball.bounce_y()
            break


screen.listen()
screen.onkey(fun=paddle.move_left, key="Left")
screen.onkey(fun=paddle.move_right, key="Right")

game_is_on = True
while game_is_on:
    ball.move()
    check_collision_with_walls()
    check_collision_with_paddle()
    check_collision_with_bricks()

    if ball.ycor() < paddle.ycor() - 50:
        game_is_on = False

    screen.update()
    time.sleep(ball.move_speed)

screen.exitonclick()
