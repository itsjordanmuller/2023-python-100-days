import time
from turtle import Screen


screen = Screen()
screen.setup(width=500, height=900)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)

screen.exitonclick()
