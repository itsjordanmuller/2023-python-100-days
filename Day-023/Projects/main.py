import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car = CarManager()

score = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car.create_car()
    car.move_across()

    screen.update()

    if player.ycor() >= FINISH_LINE_Y:
        player.reset_position()
        score.increase_level()
        car.level_up()

screen.exitonclick()
