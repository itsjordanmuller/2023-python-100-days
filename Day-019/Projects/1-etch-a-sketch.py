from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_clockwise():
    tim.right(5)


def turn_counter_clockwise():
    tim.left(5)


screen.listen()

screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_clockwise, key="d")
screen.onkey(fun=turn_counter_clockwise, key="a")


screen.exitonclick()
