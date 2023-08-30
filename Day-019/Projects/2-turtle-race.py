from turtle import Turtle, Screen
import random

screen = Screen()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet!",
    prompt="Type a color to place your bet on which turtle will win the race: ",
)
print(f"You bet on {user_bet}!")

space_between = 40
starting_y = space_between * (len(colors) - 1) / 2

turtles = []

for i, color in enumerate(colors):
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-240, y=starting_y - i * space_between)
    turtles.append(turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))

        if turtle.xcor() >= 250:
            race_on = False
            winning_color = turtle.pencolor()
            print(f"The {winning_color} turtle is the winner!")
            break


screen.exitonclick()
