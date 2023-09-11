import random
from tkinter import *

import pandas


# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"


# DATA SETUP
df = pandas.read_csv("./data/french_words.csv")
print(df)


def get_random_word():
    row = df.sample().iloc[0]
    return row["French"], row["English"]


french_word, english_word = get_random_word()


# UI SETUP
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

canvas.create_image(400, 263, image=card_front_img)

title_text = canvas.create_text(400, 150, text="Language", font=("Arial", 30, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 50, "bold"))

canvas.grid(column=0, row=0, columnspan=2)


def wrong_click():
    print("Wrong button clicked!")
    change_word()


def right_click():
    print("Right button clicked!")
    change_word()


def change_word():
    french_word, english_word = get_random_word()
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=french_word)


wrong_button = Button(
    window,
    image=wrong_img,
    command=wrong_click,
    borderwidth=0,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
)
wrong_button.grid(column=0, row=1)

right_button = Button(
    window,
    image=right_img,
    command=right_click,
    borderwidth=0,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
)
right_button.grid(column=1, row=1)

change_word()

window.mainloop()
