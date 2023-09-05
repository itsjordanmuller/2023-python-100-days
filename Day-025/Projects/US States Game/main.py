import turtle

screen = turtle.Screen()
screen.title("US States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(
    title="Guess Another State", prompt="What's another name of a state in the US?"
)

# def get_mouse_click_coor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
screen.exitonclick()
