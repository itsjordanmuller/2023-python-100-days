from tkinter import *


class UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("BMI Calculator")

        self.header_canvas = Canvas(
            self.window, width=400, height=50, bg="#718093", highlightthickness=0
        )
        self.header_canvas.grid(column=0, row=0, columnspan=2)
        self.header_canvas.create_text(
            200, 25, text="BMI CALCULATOR", font=("TkFixedFont", 18, "bold")
        )

        self.result_canvas = Canvas(
            self.window, width=400, height=300, bg="#718093", highlightthickness=0
        )
        self.result_canvas.grid(column=0, row=1, columnspan=2)
        self.result_canvas.create_text(
            200,
            30,
            text="BODY MASS INDEX",
            font=("TkFixedFont", 12, "bold"),
            fill="#353b48",
        )
        self.result_canvas.create_rectangle(50, 60, 350, 260, fill="#dcdde1", width=0)
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
            self.window, width=200, height=200, bg="#718093", highlightthickness=0
        )
        self.age_canvas.grid(column=0, row=2)
        self.age_canvas.create_text(
            100,
            30,
            text="AGE (IN YEARS)",
            font=("TkFixedFont", 12, "bold"),
            fill="#353b48",
        )
        self.age_canvas.create_rectangle(40, 55, 160, 125, fill="#dcdde1", width=0)
        self.age_canvas.create_text(
            100, 90, text="100", font=("TkFixedFont", 40, "bold")
        )
        self.age_canvas.create_oval(50, 140, 90, 180, fill="#273c75")
        self.age_canvas.create_oval(150, 140, 110, 180, fill="#273c75")

        self.weight_canvas = Canvas(
            self.window, width=200, height=200, bg="#718093", highlightthickness=0
        )
        self.weight_canvas.grid(column=1, row=2)
        self.weight_canvas.create_text(
            100,
            30,
            text="WEIGHT (POUNDS)",
            font=("TkFixedFont", 12, "bold"),
            fill="#353b48",
        )
        self.weight_canvas.create_rectangle(40, 55, 160, 125, fill="#dcdde1", width=0)
        self.weight_canvas.create_text(
            100, 90, text="150", font=("TkFixedFont", 40, "bold")
        )
        self.weight_canvas.create_oval(50, 140, 90, 180, fill="#273c75")
        self.weight_canvas.create_oval(150, 140, 110, 180, fill="#273c75")

        self.height_canvas = Canvas(
            self.window, width=200, height=200, bg="#718093", highlightthickness=0
        )
        self.height_canvas.grid(column=0, row=3)
        self.height_canvas.create_text(
            100,
            30,
            text="HEIGHT (FEET)",
            font=("TkFixedFont", 12, "bold"),
            fill="#353b48",
        )
        self.height_canvas.create_rectangle(40, 90, 90, 150, fill="#dcdde1", width=0)
        self.height_canvas.create_rectangle(110, 90, 160, 150, fill="#dcdde1", width=0)
        self.height_canvas.create_text(
            65, 112, text="5", font=("TkFixedFont", 36, "bold")
        )
        self.height_canvas.create_text(
            135, 112, text="8", font=("TkFixedFont", 36, "bold")
        )
        self.height_canvas.create_text(65, 140, text="ft", font=("TkFixedFont", 12))
        self.height_canvas.create_text(135, 140, text="in", font=("TkFixedFont", 12))
        self.height_canvas.create_oval(50, 155, 80, 185, fill="#273c75")
        self.height_canvas.create_oval(50, 55, 80, 85, fill="#273c75")
        self.height_canvas.create_oval(120, 155, 150, 185, fill="#273c75")
        self.height_canvas.create_oval(120, 55, 150, 85, fill="#273c75")

        self.gender_canvas = Canvas(
            self.window, width=200, height=200, bg="#718093", highlightthickness=0
        )
        self.gender_canvas.grid(column=1, row=3)
        self.gender_canvas.create_text(
            100,
            30,
            text="GENDER",
            font=("TkFixedFont", 12, "bold"),
            fill="#353b48",
        )
        self.gender_canvas.create_rectangle(40, 55, 160, 130, fill="#dcdde1", width=0)
        self.gender_canvas.create_text(
            100,
            75,
            text="I am",
            font=("TkFixedFont", 12, "bold"),
            fill="#353b48",
        )
        self.gender_canvas.create_text(
            100,
            100,
            text="FEMALE",
            font=("TkFixedFont", 18, "bold"),
            fill="#353b48",
        )
        self.gender_canvas.create_oval(50, 140, 90, 180, fill="#273c75")
        self.gender_canvas.create_oval(150, 140, 110, 180, fill="#273c75")

        self.window.mainloop()
