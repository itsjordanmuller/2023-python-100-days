import turtle

import pandas

screen = turtle.Screen()
screen.title("US States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_turtle = turtle.Turtle()
state_turtle.hideturtle()
state_turtle.penup()

data = pandas.read_csv("50_states.csv")
# print(data["state"])

df = pandas.DataFrame(data)
# print(df)

# 1. Get a Guess and Convert to Title Case
answer_state = (
    screen.textinput(
        title="Guess Another State", prompt="What's another name of a state in the US?"
    )
).title()

# 2. Check if Guess is Among the 50 States
# 3. Write the Correct Guesses onto the Map
if answer_state in df["state"].values:
    print(f"{answer_state} is a valid US state!")
    state_row = df[df["state"] == answer_state].iloc[0]
    state_turtle.goto(int(state_row["x"]), int(state_row["y"]))
    state_turtle.write(answer_state, align="center", font=("Arial", 8, "normal"))
else:
    print(f"{answer_state} is not a valid US state!")


# def get_mouse_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
screen.exitonclick()
