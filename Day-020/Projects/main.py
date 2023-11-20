from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initialize Snake object
snake = Snake()

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

screen.exitonclick()
