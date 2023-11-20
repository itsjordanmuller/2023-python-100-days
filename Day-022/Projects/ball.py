from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.penup()
        self.set_new_angle()  # Set initial movement angle of the ball

    def move(self, right_paddle, left_paddle, scoreboard):
        self.forward(10)  # Move the ball forward

        # Bounce off top and bottom walls
        if self.ycor() > 250 or self.ycor() < -250:
            self.bounce_wall()

        # Check if ball hits right wall
        if self.xcor() > 429:
            self.reset_position()
            scoreboard.increase_left_score()

        # Check if ball hits left wall
        if self.xcor() < -429:
            self.reset_position()
            scoreboard.increase_right_score()

        # Bounce off right paddle
        if (
            self.xcor() > right_paddle.xcor() - 10
            and self.xcor() < right_paddle.xcor() + 10
            and self.ycor() < right_paddle.ycor() + 90
            and self.ycor() > right_paddle.ycor() - 90
        ):
            self.backward(10)
            self.bounce(right_paddle)

        # Bounce off left paddle
        if (
            self.xcor() < left_paddle.xcor() + 10
            and self.xcor() > left_paddle.xcor() - 10
            and self.ycor() < left_paddle.ycor() + 90
            and self.ycor() > left_paddle.ycor() - 90
        ):
            self.backward(10)
            self.bounce(left_paddle)

    def bounce(self, paddle):
        # Change direction based on paddle contact
        offset = self.ycor() - paddle.ycor()
        new_angle = 180 - self.heading() + offset * 0.5
        self.setheading(new_angle)

    def bounce_wall(self):
        # Invert direction upon hitting a wall
        current_angle = self.heading()
        new_angle = 360 - current_angle
        self.setheading(new_angle)

    def reset_position(self):
        # Reset ball position to center after scoring
        self.goto(0, 0)
        self.set_new_angle()
        self.bounce_wall()

    def set_new_angle(self):
        # Set a new random angle for ball movement
        self.angle = random.choice([random.randint(-25, 25), random.randint(155, 205)])
        self.setheading(self.angle)
