from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


screen.listen()

screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")

screen.exitonclick()
