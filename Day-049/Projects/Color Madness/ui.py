from tkinter import *
import random


class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Color Madness")
        self.window.config(width=900, height=900)

        self.title_canvas = Canvas(
            self.window, width=1080, height=100, bg="#e5e5e5", highlightthickness=0
        )
        self.title_canvas.grid(column=0, row=0)

        self.title_canvas.create_text(
            540,
            50,
            text="COLOR MADNESS",
            fill="black",
            font=("TkFixedFont", 30, "bold"),
        )

        self.game_canvas = Canvas(
            self.window, width=1080, height=600, bg="#d4d4d4", highlightthickness=0
        )
        self.game_canvas.grid(column=0, row=1)

        self.draw_circle(475, "#525252")
        self.draw_circle(450, "#fff")
        self.draw_circle(400, "blue")

        self.control_canvas = Canvas(
            self.window, width=1080, height=200, bg="#e5e5e5", highlightthickness=0
        )
        self.control_canvas.grid(column=0, row=2)

        self.window.mainloop()

    def draw_circle(self, size, color):
        canvas_width = self.game_canvas.winfo_reqwidth()
        canvas_height = self.game_canvas.winfo_reqheight()

        x1 = (canvas_width - size) / 2
        y1 = (canvas_height - size) / 2
        x2 = x1 + size
        y2 = y1 + size

        self.game_canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)
