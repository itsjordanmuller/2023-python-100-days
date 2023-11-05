import random
from tkinter import *


class UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed Test")

        self.header_canvas = Canvas(
            self.window, width=800, height=100, highlightthickness=0
        )
        self.header_canvas.pack(fill="x")
        self.header_canvas.create_text(
            400, 50, text="Typing Speed Test", font=("TkFixedFont", 32, "bold")
        )

        self.display_canvas = Canvas(
            self.window, width=800, height=300, highlightthickness=0
        )
        self.display_canvas.pack(fill="x")

        self.shuffled_text = self.shuffle_alphabets()
        self.display_shuffled_text()

        self.typing_entry = Entry(self.window, font=("TkFixedFont", 24))
        self.typing_entry.pack(fill="x", padx=10, pady=10)

        self.timer_canvas = Canvas(
            self.window, width=800, height=150, highlightthickness=0
        )
        self.timer_canvas.pack(fill="x")
        self.timer_timer_text = self.timer_canvas.create_text(
            400, 75, text="00:00", font=("TkFixedFont", 32, "bold")
        )

        self.window.mainloop()

    def shuffle_alphabets(self):
        alphabets = list("abcdefghijklmnopqrstuvwxyz")
        random.shuffle(alphabets)
        return "".join(alphabets)

    def display_shuffled_text(self):
        self.display_canvas.create_text(
            400,
            150,
            text=self.shuffled_text,
            font=("TkFixedFont", 24, "italic"),
            fill="gray",
        )
