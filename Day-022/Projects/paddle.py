from turtle import Turtle


class Paddle(Turtle):
    """
    Represents a paddle in the Pong game.
    Handles paddle movement.
    """

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=9, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        # Move the paddle up if within screen bounds
        if self.ycor() + 90 < 262.5:
            move_y = self.ycor() + 20
            self.goto(self.xcor(), move_y)

    def move_down(self):
        # Move the paddle down if within screen bounds
        if self.ycor() - 90 > -262.5:
            move_y = self.ycor() - 20
            self.goto(self.xcor(), move_y)
