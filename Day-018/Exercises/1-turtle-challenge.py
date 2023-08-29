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


def calc_interior_angles(n):
    """Calculates the interior angles of regular shapes given a number of sides as an input n"""
    angle = ((n - 2) * 180) / n
    print(angle)


calc_interior_angles(3)


# Leave the screen/exit on click settings at the end of code
screen = Screen()
screen.exitonclick()
