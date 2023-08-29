from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("firebrick1")

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


def calc_exterior_angles(n):
    """Calculates the exterior angles of regular shapes given a number of sides as an input n"""
    angle = 360 / n
    return angle


for sides in range(3, 11):
    current_angle = calc_exterior_angles(sides)

    for step in range(0, sides):
        tim.forward(100)
        tim.right(current_angle)


# Leave the screen/exit on click settings at the end of code
screen = Screen()
screen.exitonclick()
