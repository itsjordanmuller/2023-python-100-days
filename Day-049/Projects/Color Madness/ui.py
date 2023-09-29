from tkinter import *
import random


class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Color Madness")
        self.window.config(width=900, height=900)

        self.title_canvas = Canvas(self.window, width=1080, height=100)
        self.title_canvas.grid(column=0, row=0)

        self.title_canvas.create_text(
            540, 50, text="Color Madness!", fill="black", font=("Arial", 24)
        )

        self.game_canvas = Canvas(self.window, width=1080, height=600)
        self.game_canvas.grid(column=0, row=1)

        self.control_canvas = Canvas(self.window, width=1080, height=200)
        self.control_canvas.grid(column=0, row=2)

        self.window.mainloop()
