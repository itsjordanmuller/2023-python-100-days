from turtle import Turtle


class DashedLine(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.25, stretch_len=1)
        self.penup()
        self.goto(0, 250)
        self.setheading(-90)

    def draw(self):
        for _ in range(11):
            self.stamp()
            self.forward(45)
