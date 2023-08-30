from turtle import Turtle, Screen

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

# red = Turtle(shape="turtle")
# red.penup()
# red.goto(x=-240, y=0)

screen.exitonclick()
