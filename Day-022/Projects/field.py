from turtle import Turtle


class DashedLine(Turtle):
    """
    Represents the dashed line in the middle of the Pong game field.
    """

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.25, stretch_len=1)
        self.penup()
        self.goto(0, 250)
        self.setheading(-90)

    def draw(self):
        # Draw the dashed line on the screen
        for _ in range(11):
            self.stamp()
            self.forward(45)
