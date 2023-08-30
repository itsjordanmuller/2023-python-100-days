from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet!",
    prompt="Type a color to place your bet on which turtle will win the race: ",
)
print(f"You bet on {user_bet}!")

screen.exitonclick()
