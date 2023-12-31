from turtle import Turtle
import random

# Constants for car properties
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MAX_DIFFICULTY = 7


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.difficulty = 0

    # Create a new car with a chance based on difficulty
    def create_car(self):
        chance = random.randint(1, 10 - self.difficulty)
        if chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)

    # Move all cars across the screen
    def move_across(self):
        for car in self.cars:
            car.setx(car.xcor() - self.car_speed)

    # Increase speed and difficulty when leveling up
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        if self.difficulty < MAX_DIFFICULTY:
            self.difficulty += 1

    # Calculate boundaries of a car for collision detection
    def car_boundaries(self, car):
        left = car.xcor() - 20
        right = car.xcor() + 20
        top = car.ycor() + 10
        bottom = car.ycor() - 10
        return left, right, top, bottom
