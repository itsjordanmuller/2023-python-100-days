from tkinter import *
from tkinter import messagebox
import random
import pandas
import os


# CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
FLIP_TIME = 3000


# DATA SETUP
df = pandas.read_csv("./data/french_words.csv")
# print(df)
if not os.path.exists("./data/words_to_learn.csv"):
    df.to_csv("./data/words_to_learn.csv", index=False)
else:
    df = pandas.read_csv("./data/words_to_learn.csv")


def get_random_word():
    global df

    if df.empty:
        answer = messagebox.askokcancel(
            title="Reset Words",
            message="Congrats!\nAll words learned!\nWould you like to reset the words?\nThis will add all of the words you've already learned back to the list, resetting your progress.",
        )
        if answer:  # If user clicked 'Ok'
            df = pandas.read_csv("./data/french_words.csv")
            df.to_csv("./data/words_to_learn.csv", index=False)
            row = df.sample().iloc[0]
            return row["French"], row["English"]
        else:
            return None, None
    else:
        row = df.sample().iloc[0]
        return row["French"], row["English"]


# UI SETUP
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

canvas_img = canvas.create_image(400, 263, image=card_front_img)

title_text = canvas.create_text(400, 150, text="Language", font=("Arial", 30, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 50, "bold"))

canvas.grid(column=0, row=0, columnspan=2)


def wrong_click():
    print("Wrong button clicked!")
    change_word()


def right_click():
    print("Right button clicked!")
    remove_word_from_learn_list(french_word, english_word)
    change_word()


def remove_word_from_learn_list(french, english):
    global df
    df = df[(df.French != french) & (df.English != english)]
    df.to_csv("./data/words_to_learn.csv", index=False)


after_event = None


def change_word():
    global card_state, after_event, french_word, english_word

    if after_event:
        window.after_cancel(after_event)

    if card_state == "back":
        flip_card()
    french_word, english_word = get_random_word()
    if french_word is None and english_word is None:
        print("Congrats!\nAll words learned!")
        return
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=french_word)
    after_event = window.after(FLIP_TIME, flip_card)


card_state = "front"


def flip_card():
    global card_state, french_word, english_word
    if card_state == "front":
        canvas.itemconfig(canvas_img, image=card_back_img)
        canvas.itemconfig(title_text, text="English", fill="white")
        canvas.itemconfig(word_text, text=english_word, fill="white")
        card_state = "back"
    else:
        canvas.itemconfig(canvas_img, image=card_front_img)
        canvas.itemconfig(title_text, text="French", fill="black")
        canvas.itemconfig(word_text, text=french_word, fill="black")
        card_state = "front"


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

if df.empty:
    print("Congrats!\nAll words learned!")
else:
    change_word()

window.mainloop()
