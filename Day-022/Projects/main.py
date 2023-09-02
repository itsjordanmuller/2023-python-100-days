from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=858, height=525)
screen.bgcolor("black")
screen.title("Pong Game")

right_paddle = Paddle((410, 0))
left_paddle = Paddle((-415, 0))

screen.listen()
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")
screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")

screen.exitonclick()
