from tkinter import *


class UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("BMI Calculator")

        self.header_canvas = Canvas(
            self.window, width=400, height=100, bg="red", highlightthickness=0
        )
        self.header_canvas.grid(column=0, row=0, columnspan=2)

        self.result_canvas = Canvas(
            self.window, width=400, height=200, bg="orange", highlightthickness=0
        )
        self.result_canvas.grid(column=0, row=1, columnspan=2)

        self.age_canvas = Canvas(
            self.window, width=200, height=200, bg="yellow", highlightthickness=0
        )
        self.age_canvas.grid(column=0, row=2)

        self.weight_canvas = Canvas(
            self.window, width=200, height=200, bg="green", highlightthickness=0
        )
        self.weight_canvas.grid(column=1, row=2)

        self.gender_canvas = Canvas(
            self.window, width=400, height=200, bg="blue", highlightthickness=0
        )
        self.gender_canvas.grid(column=0, row=3, columnspan=2)

        self.window.mainloop()
