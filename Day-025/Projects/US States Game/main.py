import turtle

import pandas

screen = turtle.Screen()
screen.title("US States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
# print(data["state"])

df = pandas.DataFrame(data)
print(df)

# 1. Get a Guess and Convert to Title Case
answer_state = (
    screen.textinput(
        title="Guess Another State", prompt="What's another name of a state in the US?"
    )
).title()

# 2. Check if Guess is Among the 50 States

# def get_mouse_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
screen.exitonclick()
