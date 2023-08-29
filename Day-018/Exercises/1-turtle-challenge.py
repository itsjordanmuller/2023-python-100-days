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

for i in range(50):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

# Leave the screen/exit on click settings at the end of code
screen = Screen()
screen.exitonclick()
