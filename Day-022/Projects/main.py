from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
from field import DashedLine
import time

# Set up the game screen
screen = Screen()
screen.setup(width=858, height=525)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Initialize paddles
right_paddle = Paddle((410, 0))
left_paddle = Paddle((-415, 0))

# Draw the midline
dashed_line = DashedLine()
dashed_line.draw()

# Initialize ball and scoreboard
ball = Ball()
score = Scoreboard()

# Setup keyboard controls
screen.listen()
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")
screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")

# Main game loop
game_is_on = True
while game_is_on:
    ball.move(right_paddle, left_paddle, score)
    screen.update()
    time.sleep(0.05)
    if score.game_is_over:
        game_is_on = False

screen.exitonclick()
