import colorgram
import random
from turtle import Turtle, Screen


def draw_spot(position, color, size=5):
    painter.penup()
    painter.color(color)
    painter.goto(position)
    painter.pendown()
    painter.begin_fill()
    painter.circle(size)
    painter.end_fill()


colors = colorgram.extract("damien-hirst-spots.jpg", 30)
color_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

# for color in colors:
#     r, g, b = color.rgb
#     print(f"({r}, {g}, {b})")

screen = Screen()
screen.bgcolor("white")
screen.colormode(255)

painter = Turtle()
painter.speed(10)

grid_spacing = 30
grid_size = 5

for x in range(
    -(grid_spacing * grid_size) // 2, (grid_spacing * grid_size) // 2, grid_spacing
):
    for y in range(
        -(grid_spacing * grid_size) // 2, (grid_spacing * grid_size) // 2, grid_spacing
    ):
        color = random.choice(color_list)
        draw_spot((x, y), color)

screen.exitonclick()
