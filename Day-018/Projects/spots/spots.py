import colorgram
import random
from turtle import Turtle, Screen

colors = colorgram.extract("damien-hirst-spots.jpg", 30)
color_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

# for color in colors:
#     r, g, b = color.rgb
#     print(f"({r}, {g}, {b})")

screen = Screen()
screen.bgcolor("white")

painter = Turtle()
painter.speed(10)

screen.exitonclick()
