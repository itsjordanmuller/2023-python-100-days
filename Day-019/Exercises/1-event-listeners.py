from turtle import Turtle, Screen


# Define function to move turtle forward by 10 units
def move_forwards():
    tim.forward(10)


# Initialize turtle object and create screen
tim = Turtle()
screen = Screen()

# Listen for events on screen
screen.listen()

# Bind space key to move_forwards function
screen.onkey(fun=move_forwards, key="space")

# Exit program on screen click
screen.exitonclick()
