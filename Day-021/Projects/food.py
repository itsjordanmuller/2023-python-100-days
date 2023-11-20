from turtle import Turtle
import random


class Food(Turtle):
    """Creates and handles pieces of food in the Snake game."""

    def __init__(self):
        """Initialize the food with default properties."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Reposition the food to a random location on the screen."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
