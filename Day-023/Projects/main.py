import time
from turtle import Screen

from car_manager import CarManager
from player import Player, FINISH_LINE_Y
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car = CarManager()

score = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")


def check_collision(player_bounds, car_bounds):
    p_left, p_right, p_top, p_bottom = player_bounds
    c_left, c_right, c_top, c_bottom = car_bounds

    return not (
        p_left > c_right or p_right < c_left or p_top < c_bottom or p_bottom > c_top
    )


game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car.create_car()
    car.move_across()

    player_bounds = player.boundaries()

    for each_car in car.cars:
        car_bounds = car.car_boundaries(each_car)
        if check_collision(player_bounds, car_bounds):
            game_is_on = False
            score.game_over()

    screen.update()
    # score.game_over()

    if player.ycor() >= FINISH_LINE_Y:
        player.reset_position()
        score.increase_level()
        car.level_up()

screen.exitonclick()
