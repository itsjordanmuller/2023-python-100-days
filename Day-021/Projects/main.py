from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_right, "d")
screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        print(f"Pieces eaten: {scoreboard.score}")

    if (
        snake.head.xcor() > 300
        or snake.head.xcor() < -300
        or snake.head.ycor() > 300
        or snake.head.ycor() < -300
    ):
        game_is_on = False
        scoreboard.game_over()
        print(f"Game over. You got a final score of: {scoreboard.score}")

    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        # elif snake.head.distance(segment[1:]) < 10:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            print(f"Game over. You got a final score of: {scoreboard.score}")

screen.exitonclick()
