from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
# tim.color("firebrick1")

# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)

# for i in range(50):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


def random_color():
    """Generates a random color using RGB color format"""
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r, g, b


def calc_exterior_angles(n):
    """Calculates the exterior angles of regular shapes given a number of sides as an input n"""
    angle = 360 / n
    return angle


def random_angle():
    """Returns a random angle in multiples of 90 degrees, options include: (90deg, 180deg, 270deg)"""
    turns = random.randint(1, 3)
    turn_angle = turns * 90
    return turn_angle


# Leave the screen/exit on click settings at the end of code
screen = Screen()

screen.colormode(255)

# Draw Shapes with 3 Sides to 10 Sides Challenge

# for sides in range(3, 11):
#     tim.color(random_color())
#     current_angle = calc_exterior_angles(sides)

#     for step in range(0, sides):
#         tim.forward(100)
#         tim.right(current_angle)

# Random Walk Challenge

# tim.pensize(5)
# tim.speed(10)

# for i in range(1, 501):
#     tim.color(random_color())
#     direction = random.randint(0, 1)
#     if direction == 0:
#         tim.left(random_angle())
#     else:
#         tim.right(random_angle())
#     tim.forward(10)

# Spirograph Challenge


screen.exitonclick()
