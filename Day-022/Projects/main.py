from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=858, height=525)
screen.bgcolor("black")
screen.title("Pong Game")

right_paddle = Paddle((410, 0))

screen.exitonclick()
