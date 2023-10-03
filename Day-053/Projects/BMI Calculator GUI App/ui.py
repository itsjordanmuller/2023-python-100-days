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
        self.weight_canvas.create_text(
            100,
            30,
            text="WEIGHT (POUNDS)",
            font=("TkFixedFont", 12, "bold"),
            fill="#353b48",
        )
        self.weight_canvas.create_rectangle(40, 55, 160, 125, fill="white")
        self.weight_canvas.create_text(
            100, 90, text="150", font=("TkFixedFont", 40, "bold")
        )
        self.weight_canvas.create_oval(50, 140, 90, 180, fill="#718093")
        self.weight_canvas.create_oval(150, 140, 110, 180, fill="#718093")

        self.height_canvas = Canvas(
            self.window, width=200, height=200, bg="blue", highlightthickness=0
        )
        self.height_canvas.grid(column=0, row=3)
        self.height_canvas.create_text(
            100,
            30,
            text="HEIGHT (FEET)",
            font=("TkFixedFont", 12, "bold"),
            fill="#353b48",
        )
        self.height_canvas.create_rectangle(40, 90, 90, 150, fill="white")
        self.height_canvas.create_rectangle(110, 90, 160, 150, fill="white")
        self.height_canvas.create_text(
            65, 112, text="5", font=("TkFixedFont", 36, "bold")
        )
        self.height_canvas.create_text(
            135, 112, text="8", font=("TkFixedFont", 36, "bold")
        )
        self.height_canvas.create_text(65, 140, text="ft", font=("TkFixedFont", 12))
        self.height_canvas.create_text(135, 140, text="in", font=("TkFixedFont", 12))
        self.height_canvas.create_oval(50, 155, 80, 185, fill="#718093")
        self.height_canvas.create_oval(50, 55, 80, 85, fill="#718093")
        self.height_canvas.create_oval(120, 155, 150, 185, fill="#718093")
        self.height_canvas.create_oval(120, 55, 150, 85, fill="#718093")

        self.gender_canvas = Canvas(
            self.window, width=200, height=200, bg="purple", highlightthickness=0
        )
        self.gender_canvas.grid(column=1, row=3)

        self.window.mainloop()
