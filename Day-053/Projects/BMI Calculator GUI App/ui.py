from tkinter import *


class UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("BMI Calculator")

        self.header_canvas = Canvas(
            self.window, width=400, height=50, bg="red", highlightthickness=0
        )
        self.header_canvas.grid(column=0, row=0, columnspan=2)
        self.header_canvas.create_text(
            200, 25, text="BMI CALCULATOR", font=("TkFixedFont", 18, "bold")
        )

        self.result_canvas = Canvas(
            self.window, width=400, height=300, bg="orange", highlightthickness=0
        )
        self.result_canvas.grid(column=0, row=1, columnspan=2)
        self.result_canvas.create_text(
            200,
            30,
            text="BODY MASS INDEX",
            font=("TkFixedFont", 12, "bold"),
            fill="#353b48",
        )
        self.result_canvas.create_rectangle(50, 60, 350, 260, fill="white")
        self.result_canvas.create_text(
            200, 135, text="22.5", font=("TkFixedFont", 96, "bold")
        )
        self.result_canvas.create_text(
            200,
            220,
            text="HEALTHY",
            font=("TkFixedFont", 24, "bold"),
            fill="#353b48",
        )

        self.age_canvas = Canvas(
            self.window, width=200, height=200, bg="yellow", highlightthickness=0
        )
        self.age_canvas.grid(column=0, row=2)
        self.age_canvas.create_text(
            100,
            30,
            text="AGE (IN YEARS)",
            font=("TkFixedFont", 12, "bold"),
            fill="#353b48",
        )
        self.age_canvas.create_rectangle(40, 55, 160, 125, fill="white")
        self.age_canvas.create_text(
            100, 90, text="100", font=("TkFixedFont", 40, "bold")
        )
        self.age_canvas.create_oval(50, 140, 90, 180, fill="#718093")
        self.age_canvas.create_oval(150, 140, 110, 180, fill="#718093")

        self.weight_canvas = Canvas(
            self.window, width=200, height=200, bg="green", highlightthickness=0
        )
        self.weight_canvas.grid(column=1, row=2)

        self.gender_canvas = Canvas(
            self.window, width=400, height=200, bg="blue", highlightthickness=0
        )
        self.gender_canvas.grid(column=0, row=3, columnspan=2)

        self.window.mainloop()
