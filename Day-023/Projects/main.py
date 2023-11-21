import time
from turtle import Screen

from car_manager import CarManager
from player import Player, FINISH_LINE_Y
from scoreboard import Scoreboard

# Setup main game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")

# Initialize player, car manager, and scoreboard
player = Player()
car = CarManager()
score = Scoreboard()

# Screen event listeners
screen.listen()
screen.onkey(fun=player.move_up, key="Up")


# Check for collision between player and car
def check_collision(player_bounds, car_bounds):
    p_left, p_right, p_top, p_bottom = player_bounds
    c_left, c_right, c_top, c_bottom = car_bounds
    return not (
        p_left > c_right or p_right < c_left or p_top < c_bottom or p_bottom > c_top
    )


# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.create_car()
    car.move_across()

    # Get player boundaries for collision detection
    player_bounds = player.boundaries()

    # Check for collision with each car
    for each_car in car.cars:
        car_bounds = car.car_boundaries(each_car)
        if check_collision(player_bounds, car_bounds):
            game_is_on = False
            break

    # Update screen
    screen.update()

    # Display game over message if collision occurs
    if not game_is_on:
        score.game_over()

    # Check if player crosses finish line
    if player.ycor() >= FINISH_LINE_Y:
        player.reset_position()
        score.increase_level()
        car.level_up()

# Exit on click
screen.exitonclick()
