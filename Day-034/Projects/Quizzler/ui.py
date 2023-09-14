from tkinter import *

THEME_COLOR = "#375362"

question_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean velit?"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)

        self.score_label = Label(
            text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12)
        )
        self.score_label.grid(column=1, row=0, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.create_text(
            150,
            125,
            text=question_text,
            font=("Arial", 15, "italic"),
            width=260,
            justify="center",
        )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.true_image = PhotoImage(file="./images/true.png")
        self.false_image = PhotoImage(file="./images/false.png")

        self.true_button = Button(
            self.window,
            image=self.true_image,
            borderwidth=0,
            bg=THEME_COLOR,
            highlightthickness=0,
        )
        self.true_button.grid(column=0, row=2, pady=20, padx=20, sticky="E")

        self.false_button = Button(
            self.window,
            image=self.false_image,
            borderwidth=0,
            bg=THEME_COLOR,
            highlightthickness=0,
        )
        self.false_button.grid(column=1, row=2, pady=20, padx=20, sticky="W")

        self.window.mainloop()
