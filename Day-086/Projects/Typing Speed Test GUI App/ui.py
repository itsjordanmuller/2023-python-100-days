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
            self.window, width=800, height=200, highlightthickness=0
        )
        self.display_canvas.pack(fill="x")

        self.shuffled_text = self.shuffle_alphabets()
        self.letter_ids = []
        self.display_shuffled_text()

        self.typing_entry = Entry(self.window, font=("TkFixedFont", 24))
        self.typing_entry.pack(fill="x", padx=10, pady=10)
        self.typing_entry.bind("<KeyRelease>", self.on_key_release)

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
        x_offset = 272 - (len(self.shuffled_text) * 7)
        for index, letter in enumerate(self.shuffled_text):
            letter_id = self.display_canvas.create_text(
                x_offset + (index * 25),
                100,
                text=letter,
                font=("Courier", 24),
                fill="gray",
                tags="shuffled_letter",
            )
            self.letter_ids.append(letter_id)

    def on_key_release(self, event):
        typed_text = self.typing_entry.get()
        for index, letter_id in enumerate(self.letter_ids):
            if index < len(typed_text):
                letter_color = (
                    "green" if self.shuffled_text[index] == typed_text[index] else "red"
                )
                self.display_canvas.itemconfig(letter_id, fill=letter_color)
            else:
                self.display_canvas.itemconfig(letter_id, fill="gray")
