from tkinter import *


class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Rock Paper Scissors")

        # Paper icons created by Freepik - Flaticon
        # https://www.flaticon.com/free-icons/paper
        self.paper_img = PhotoImage(file="./images/scroll.png").subsample(5, 5)

        # Rock icons created by Freepik - Flaticon
        # https://www.flaticon.com/free-icons/rock
        self.rock_img = PhotoImage(file="./images/stone.png").subsample(5, 5)

        # Scissors icons created by Freepik - Flaticon
        # https://www.flaticon.com/free-icons/scissors
        self.scissors_img = PhotoImage(file="./images/scissors.png").subsample(5, 5)

        self.score_canvas = Canvas(
            self.window,
            width=448,
            height=64,
            highlightthickness=0,
            borderwidth=0,
            bg="red",
        )
        self.score_canvas.grid(column=0, row=0, columnspan=3)

        self.game_canvas = Canvas(
            self.window,
            width=448,
            height=448,
            highlightthickness=0,
            borderwidth=0,
            bg="orange",
        )
        self.game_canvas.grid(column=0, row=1, columnspan=3)

        self.button_canvas = Canvas(
            self.window,
            width=448,
            height=192,
            highlightthickness=0,
            borderwidth=0,
            bg="#2c3e50",
        )

        self.rock_button = Button(
            self.button_canvas,
            image=self.rock_img,
            borderwidth=0,
            highlightthickness=0,
            relief=FLAT,
            bg="#2c3e50",
            activebackground="#2c3e50",
        )
        self.button_canvas.create_window(84, 80, window=self.rock_button)

        self.paper_button = Button(
            self.button_canvas,
            image=self.paper_img,
            borderwidth=0,
            highlightthickness=0,
            relief=FLAT,
            bg="#2c3e50",
            activebackground="#2c3e50",
        )
        self.button_canvas.create_window(224, 80, window=self.paper_button)

        self.button_canvas.grid(column=0, row=2, columnspan=3)

        self.window.mainloop()
