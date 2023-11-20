import colorgram
import random
from turtle import Turtle, Screen


def draw_spot(position, color, size=5):
    """
    Draw a colored spot at a given position using Turtle graphics.

    Args:
        position (tuple): The (x, y) coordinates for the spot's position.
        color (tuple): The RGB color value for the spot, e.g., (255, 255, 255) for white.
        size (int, optional): The radius of the spot in pixels. Defaults to 5.
    """
    painter.penup()
    painter.color(color)
    painter.goto(position)
    painter.pendown()
    painter.begin_fill()
    painter.circle(size)
    painter.end_fill()

# Extract colors from image and create color list
colors = colorgram.extract("damien-hirst-spots.jpg", 30)
color_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

# Screen setup
screen = Screen()
screen.bgcolor("white")
screen.colormode(255)

# Turtle setup for drawing
painter = Turtle()
painter.speed(10)

# Grid configuration
grid_spacing = 30
grid_size = 10

# Drawing spots in a grid pattern
for x in range(-(grid_spacing * grid_size) // 2, (grid_spacing * grid_size) // 2, grid_spacing):
    for y in range(-(grid_spacing * grid_size) // 2, (grid_spacing * grid_size) // 2, grid_spacing):
        color = random.choice(color_list)
        draw_spot((x, y), color)

# Hide the turtle icon after drawing is complete
painter.hideturtle()

# Wait for a mouse click to exit
screen.exitonclick()