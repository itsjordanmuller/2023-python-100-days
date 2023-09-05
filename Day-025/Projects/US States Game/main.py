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
# 2. Check if Guess is Among the 50 States
# 3. Write the Correct Guesses onto the Map
# 4. Create a Loop to Allow the User to Keep Guessing
# 5. Record the Correct Guesses in a List
# 6. Keep Track of Score in Title of Prompt

guessed_states = []

game_is_on = True

while game_is_on:
    answer_state = (
        screen.textinput(
            title=f"{len(guessed_states)}/50 States Guessed",
            prompt="What's another name of a state in the US?",
        )
    ).title()

    if answer_state in guessed_states:
        print(f"You already guessed {answer_state}!")
        continue

    if answer_state in df["state"].values:
        guessed_states.append(answer_state)
        print(f"{answer_state} is a valid US state!")
        state_row = df[df["state"] == answer_state].iloc[0]
        state_turtle.goto(int(state_row["x"]), int(state_row["y"]))
        state_turtle.write(answer_state, align="center", font=("Arial", 8, "normal"))

        if len(guessed_states) == 50:
            print("Congratulations! You've guessed all 50 states!")
            game_is_on = False

    else:
        print(f"{answer_state} is not a valid US state!")


# def get_mouse_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
screen.exitonclick()
