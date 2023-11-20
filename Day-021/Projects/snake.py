from turtle import Turtle


class Snake:
    """Creates and handles the snake in the Snake game."""

    def __init__(self):
        """Initialize the snake with default properties and a head."""
        self.segments = []
        self.create_snake()
        self.direction = "right"
        self.head = self.segments[0]

    def create_snake(self):
        """Create initial snake body segments."""
        for i in range(3):
            x_position = i * -20
            self.add_segment(x_position, 0)

    def add_segment(self, x, y):
        """Add a new segment to the snake at the specified coordinates."""
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(x, y)
        self.segments.append(segment)

    def extend(self):
        """Extend the snake by adding a new segment at its tail."""
        x, y = self.segments[-1].position()
        self.add_segment(x, y)

    def move(self):
        """Move the snake forward in its current direction.

        Each segment of the snake moves to the position of the segment in front of it.
        The head of the snake moves forward in the current direction.
        """
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
        """Change the snake's direction to left if not moving right."""
        if self.direction != "right":
            self.direction = "left"

    def move_right(self):
        """Change the snake's direction to right if not moving left."""
        if self.direction != "left":
            self.direction = "right"

    def move_up(self):
        """Change the snake's direction to up if not moving down."""
        if self.direction != "down":
            self.direction = "up"

    def move_down(self):
        """Change the snake's direction to down if not moving up."""
        if self.direction != "up":
            self.direction = "down"
