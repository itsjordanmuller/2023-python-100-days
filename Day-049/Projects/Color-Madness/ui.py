from tkinter import *
from colors import color_dict, get_random_color
import json
import random


class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Color Madness")
        self.window.config(width=900, height=900)

        self.color_counter = 0

        self.title_canvas = Canvas(
            self.window, width=1080, height=100, bg="#e5e5e5", highlightthickness=0
        )
        self.title_canvas.grid(column=0, row=0, columnspan=11)

        self.title_canvas.create_text(
            540,
            30,
            text="COLOR MADNESS",
            fill="black",
            font=("TkFixedFont", 36, "bold"),
        )

        self.title_canvas.create_text(
            540,
            75,
            text="Select Which Color Best Describes the Color in the Circle",
            fill="black",
            font=("TkFixedFont", 18, "bold"),
        )

        self.game_canvas = Canvas(
            self.window, width=1080, height=700, bg="#d4d4d4", highlightthickness=0
        )
        self.game_canvas.grid(column=0, row=1, columnspan=11)

        self.draw_circle(575, "#525252")
        self.draw_circle(550, "#fff")
        self.draw_circle(500, get_random_color())

        initial_color = self.game_canvas.itemcget(self.circle, "fill")
        closest_colors = sorted(
            color_dict.values(), key=lambda x: self.color_distance(x, initial_color)
        )[:2]

        self.left_suggestive_button = Button(
            self.window,
            bg=closest_colors[0],
            text="",
            font=("TkFixedFont", 16, "bold"),
            borderwidth=0,
            highlightthickness=0,
            width=5,
        )
        self.left_suggestive_button.grid(column=0, row=1, sticky=NSEW)

        self.right_suggestive_button = Button(
            self.window,
            bg=closest_colors[1],
            text="",
            font=("TkFixedFont", 16, "bold"),
            borderwidth=0,
            highlightthickness=0,
            width=5,
        )
        self.right_suggestive_button.grid(column=10, row=1, sticky=NSEW)

        self.control_canvas = Canvas(
            self.window, width=1080, height=100, bg="#e5e5e5", highlightthickness=0
        )
        self.control_canvas.grid(column=0, row=2, columnspan=11)

        self.color_canvases = []

        for index, (color_name, hex_code) in enumerate(color_dict.items()):
            button = Button(
                self.window,
                bg=hex_code,
                text=color_name,
                font=("TkFixedFont", 16, "bold"),
                borderwidth=0,
                highlightthickness=0,
                width=5,
                command=lambda c=color_name: self.log_color_choice(c),
            )
            button.grid(column=index, row=2, sticky=NSEW)

            if color_name == "Black":
                button.config(fg="white")
                button.bind("<Enter>", self.black_on_enter)
                button.bind("<Leave>", self.black_on_leave)

            self.color_canvases.append(button)

        self.window.mainloop()

    def black_on_enter(self, e):
        e.widget.config(fg="black")

    def black_on_leave(self, e):
        e.widget.config(fg="white")

    def log_color_choice(self, color):
        color_data = self.load_color_data()
        current_color = self.game_canvas.itemcget(self.circle, "fill")

        if current_color not in color_data:
            color_data[current_color] = {}

        if color in color_data[current_color]:
            color_data[current_color][color] += 1
        else:
            color_data[current_color][color] = 1

        self.save_color_data(color_data)
        self.color_counter += 1

        if self.color_counter % 2 == 0 and color_data:
            old_colors = list(color_data.keys())
            next_color = random.choice(old_colors)
        else:
            next_color = get_random_color()

        closest_colors = sorted(
            color_dict.values(), key=lambda x: self.color_distance(x, next_color)
        )[:2]

        self.update_suggestive_buttons(closest_colors)

        self.game_canvas.itemconfig(self.circle, fill=next_color)

    def load_color_data(self):
        try:
            with open("color_data.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_color_data(self, color_data):
        with open("color_data.json", "w") as file:
            json.dump(color_data, file, indent=2)

    def draw_circle(self, size, color):
        canvas_width = self.game_canvas.winfo_reqwidth()
        canvas_height = self.game_canvas.winfo_reqheight()

        x1 = (canvas_width - size) / 2
        y1 = (canvas_height - size) / 2
        x2 = x1 + size
        y2 = y1 + size

        self.circle = self.game_canvas.create_oval(
            x1, y1, x2, y2, fill=color, outline=color
        )

    def color_distance(self, color1, color2):
        r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
        r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)

        return ((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2) ** 0.5

    def update_suggestive_buttons(self, colors):
        self.left_suggestive_button.config(
            bg=colors[0],
            command=lambda: self.log_color_choice(self.get_color_name(colors[0])),
        )
        self.right_suggestive_button.config(
            bg=colors[1],
            command=lambda: self.log_color_choice(self.get_color_name(colors[1])),
        )

    def get_color_name(self, hex_color):
        return next(
            (name for name, hex in color_dict.items() if hex == hex_color), "Unknown"
        )
