from turtle import Turtle

# Constants for player starting position and movement
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        # Player appearance and initial setup
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.reset_position()

    # Move player upwards
    def move_up(self):
        move_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), move_y)

    # Reset player position
    def reset_position(self):
        self.goto(STARTING_POSITION)

    # Calculate player boundaries for collision detection
    def boundaries(self):
        left = self.xcor() - 10
        right = self.xcor() + 10
        top = self.ycor() + 10
        bottom = self.ycor() - 10
        return left, right, top, bottom
