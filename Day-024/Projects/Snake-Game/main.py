from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Initialize screen, set title, background
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Stop screen from updating in real time
screen.tracer(0)

# Initialize game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Keyboard bindings for snake movement
screen.listen()
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_right, "d")
screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_down, "s")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Check for collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        print(f"Pieces eaten: {scoreboard.score}")

    # Check for collision with walls
    if (
        snake.head.xcor() > 300
        or snake.head.xcor() < -300
        or snake.head.ycor() > 300
        or snake.head.ycor() < -300
    ):
        scoreboard.reset()
        snake.reset_snake()

    # Check for collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()
