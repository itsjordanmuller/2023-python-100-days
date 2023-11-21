import turtle
import pandas

# Set up the screen for the game
screen = turtle.Screen()
screen.title("US States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Initialize turtle for displaying state names
state_turtle = turtle.Turtle()
state_turtle.hideturtle()
state_turtle.penup()

# Load state data from CSV file
data = pandas.read_csv("50_states.csv")

# Create a DataFrame from the loaded data
df = pandas.DataFrame(data)

# List to store guessed states
guessed_states = []

# Flag to control the game loop
game_is_on = True

# Main game loop
while game_is_on:
    answer_state = (
        screen.textinput(
            title=f"{len(guessed_states)}/50 States Guessed",
            prompt="What's another name of a state in the US?",
        )
    ).title()

    # Check if state already guessed
    if answer_state in guessed_states:
        print(f"You already guessed {answer_state}!")
        continue

    # Validate and process the guessed state
    if answer_state in df["state"].values:
        guessed_states.append(answer_state)
        print(f"{answer_state} is a valid US state!")
        state_row = df[df["state"] == answer_state].iloc[0]
        state_turtle.goto(int(state_row["x"]), int(state_row["y"]))
        state_turtle.write(answer_state, align="center", font=("Arial", 8, "normal"))

        # Check if all states have been guessed
        if len(guessed_states) == 50:
            print("Congratulations! You've guessed all 50 states!")
            game_is_on = False

    else:
        print(f"{answer_state} is not a valid US state!")

# Close the screen on click
screen.exitonclick()
