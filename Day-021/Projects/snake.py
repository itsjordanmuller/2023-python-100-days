from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.direction = "right"
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            x_position = i * -20
            self.add_segment(x_position, 0)

    def add_segment(self, x, y):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(x, y)
        self.segments.append(segment)

    def extend(self):
        x, y = self.segments[-1].position()
        self.add_segment(x, y)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)

        if self.direction == "up":
            self.segments[0].setheading(90)
        elif self.direction == "down":
            self.segments[0].setheading(270)
        elif self.direction == "left":
            self.segments[0].setheading(180)
        elif self.direction == "right":
            self.segments[0].setheading(0)

        self.segments[0].forward(20)

    def move_left(self):
        if self.direction != "right":
            self.direction = "left"

    def move_right(self):
        if self.direction != "left":
            self.direction = "right"

    def move_up(self):
        if self.direction != "down":
            self.direction = "up"

    def move_down(self):
        if self.direction != "up":
            self.direction = "down"
