from turtle import Turtle, Screen

# Create turtle and screen objects
tim = Turtle()
screen = Screen()


# Move turtle forward by 10 units
def move_forwards():
    tim.forward(10)


# Move turtle backward by 10 units
def move_backwards():
    tim.backward(10)


# Rotate turtle clockwise by 10 degrees
def turn_clockwise():
    tim.right(10)


# Rotate turtle counterclockwise by 10 degrees
def turn_counter_clockwise():
    tim.left(10)


# Clear turtle's drawings from screen
def clear_screen():
    tim.clear()


# Reset turtle's position and clear drawings
def full_reset():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# Listen for key presses
screen.listen()

# Bind keys to corresponding functions
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_clockwise, key="d")
screen.onkey(fun=turn_counter_clockwise, key="a")
screen.onkey(fun=clear_screen, key="c")
screen.onkey(fun=full_reset, key="r")

# Exit on screen click
screen.exitonclick()
