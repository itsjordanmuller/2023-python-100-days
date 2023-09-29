from tkinter import *
import random


class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Color Madness")
        self.window.config(width=900, height=900)

        colors = [
            "White",
            "Pink",
            "Red",
            "Brown",
            "Orange",
            "Yellow",
            "Green",
            "Blue",
            "Purple",
            "Grey",
            "Black",
        ]

        self.title_canvas = Canvas(
            self.window, width=1080, height=100, bg="#e5e5e5", highlightthickness=0
        )
        self.title_canvas.grid(column=0, row=0, columnspan=11)

        self.title_canvas.create_text(
            540,
            50,
            text="COLOR MADNESS",
            fill="black",
            font=("TkFixedFont", 30, "bold"),
        )

        self.game_canvas = Canvas(
            self.window, width=1080, height=700, bg="#d4d4d4", highlightthickness=0
        )
        self.game_canvas.grid(column=0, row=1, columnspan=11)

        self.draw_circle(475, "#525252")
        self.draw_circle(450, "#fff")
        self.draw_circle(400, get_random_color())

        self.control_canvas = Canvas(
            self.window, width=1080, height=100, bg="#e5e5e5", highlightthickness=0
        )
        self.control_canvas.grid(column=0, row=2, columnspan=11)

        self.color_canvases = []

        for index, color in enumerate(colors):
            button = Button(
                self.window,
                bg=color,
                text=color,
                font=("TkFixedFont", 16, "bold"),
                borderwidth=0,
                highlightthickness=0,
                width=5,
            )
            button.grid(column=index, row=2, sticky=NSEW)

            if color == "Black":
                button.config(fg="white")
                button.bind("<Enter>", self.black_on_enter)
                button.bind("<Leave>", self.black_on_leave)

            self.color_canvases.append(button)

        self.window.mainloop()

    def black_on_enter(self, e):
        e.widget.config(fg="black")

    def black_on_leave(self, e):
        e.widget.config(fg="white")

    def draw_circle(self, size, color):
        canvas_width = self.game_canvas.winfo_reqwidth()
        canvas_height = self.game_canvas.winfo_reqheight()

        x1 = (canvas_width - size) / 2
        y1 = (canvas_height - size) / 2
        x2 = x1 + size
        y2 = y1 + size

        self.game_canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return "#{:02x}{:02x}{:02x}".format(r, g, b)
