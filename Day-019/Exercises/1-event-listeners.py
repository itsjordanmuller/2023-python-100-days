from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(fun=move_forwards, key="space")
screen.exitonclick()
