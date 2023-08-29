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


# Leave the screen/exit on click settings at the end of code
screen = Screen()

screen.colormode(255)

# for sides in range(3, 11):
#     tim.color(random_color())
#     current_angle = calc_exterior_angles(sides)

#     for step in range(0, sides):
#         tim.forward(100)
#         tim.right(current_angle)


screen.exitonclick()
