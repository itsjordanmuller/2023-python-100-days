from tkinter import *
from calc import calculate_bmi, get_bmi_category


class UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("BMI Calculator")

        self.weight = 150
        self.height_feet = 5
        self.height_inches = 8
        self.bmi_color = "#64BA46"

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
        self.result_canvas.create_rectangle(
            45,
            55,
            355,
            265,
            fill=self.bmi_color,
            width=0,
            tags="bmi_rectangle",
        )
        self.result_canvas.create_rectangle(
            55,
            65,
            345,
            255,
            fill="#dcdde1",
            width=0,
        )
        self.bmi_text = self.result_canvas.create_text(
            200, 135, text="", font=("TkFixedFont", 96, "bold")
        )
        self.category_text = self.result_canvas.create_text(
            200, 220, text="", font=("TkFixedFont", 24, "bold"), fill="#353b48"
        )

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
        self.weight_text = self.weight_canvas.create_text(
            100, 90, text=str(self.weight), font=("TkFixedFont", 40, "bold")
        )
        self.weight_canvas.create_oval(
            77, 150, 97, 170, fill="#273c75", tags="decrement_weight"
        )
        self.weight_canvas.create_oval(
            123, 150, 103, 170, fill="#273c75", tags="increment_weight"
        )
        self.weight_canvas.create_oval(
            30, 140, 70, 180, fill="#273c75", tags="decrement_weight5"
        )
        self.weight_canvas.create_oval(
            170, 140, 130, 180, fill="#273c75", tags="increment_weight5"
        )
        self.weight_canvas.create_text(
            87,
            160,
            text="-",
            font=("TkFixedFont", 16, "bold"),
            fill="white",
            tags=("decrement_weight", "text"),
        )
        self.weight_canvas.create_text(
            113,
            160,
            text="+",
            font=("TkFixedFont", 16, "bold"),
            fill="white",
            tags=("increment_weight", "text"),
        )
        self.weight_canvas.create_text(
            50,
            160,
            text="-",
            font=("TkFixedFont", 26, "bold"),
            fill="white",
            tags=("decrement_weight5", "text"),
        )
        self.weight_canvas.create_text(
            150,
            160,
            text="+",
            font=("TkFixedFont", 26, "bold"),
            fill="white",
            tags=("increment_weight5", "text"),
        )

        self.height_canvas = Canvas(
            self.window, width=200, height=200, bg="#718093", highlightthickness=0
        )
        self.height_canvas.grid(column=0, row=2)
        self.height_canvas.create_text(
            100,
            30,
            text="HEIGHT (FEET)",
            font=("TkFixedFont", 12, "bold"),
            fill="#353b48",
        )
        self.height_canvas.create_rectangle(35, 90, 95, 150, fill="#dcdde1", width=0)
        self.height_canvas.create_rectangle(105, 90, 165, 150, fill="#dcdde1", width=0)
        self.feet_text = self.height_canvas.create_text(
            65, 112, text=str(self.height_feet), font=("TkFixedFont", 36, "bold")
        )
        self.inches_text = self.height_canvas.create_text(
            135, 112, text=str(self.height_inches), font=("TkFixedFont", 36, "bold")
        )
        self.height_canvas.create_text(65, 140, text="ft", font=("TkFixedFont", 12))
        self.height_canvas.create_text(135, 140, text="in", font=("TkFixedFont", 12))
        self.height_canvas.create_oval(
            50, 155, 80, 185, fill="#273c75", tags="decrement_feet"
        )
        self.height_canvas.create_oval(
            50, 55, 80, 85, fill="#273c75", tags="increment_feet"
        )
        self.height_canvas.create_oval(
            120, 155, 150, 185, fill="#273c75", tags="decrement_inches"
        )
        self.height_canvas.create_oval(
            120, 55, 150, 85, fill="#273c75", tags="increment_inches"
        )
        self.height_decrement_feet_text = self.height_canvas.create_text(
            65,
            170,
            text="-",
            font=("TkFixedFont", 20, "bold"),
            fill="white",
            tags=("decrement_feet", "text"),
        )
        self.height_increment_feet_text = self.height_canvas.create_text(
            65,
            70,
            text="+",
            font=("TkFixedFont", 20, "bold"),
            fill="white",
            tags=("increment_feet", "text"),
        )
        self.height_decrement_inches_text = self.height_canvas.create_text(
            135,
            170,
            text="-",
            font=("TkFixedFont", 20, "bold"),
            fill="white",
            tags=("decrement_inches", "text"),
        )
        self.height_increment_inches_text = self.height_canvas.create_text(
            135,
            70,
            text="+",
            font=("TkFixedFont", 20, "bold"),
            fill="white",
            tags=("increment_inches", "text"),
        )

        binds = {
            "increment_weight": {"<Button-1>": self.increment_weight},
            "decrement_weight": {"<Button-1>": self.decrement_weight},
            "increment_weight5": {"<Button-1>": self.increment_weight5},
            "decrement_weight5": {"<Button-1>": self.decrement_weight5},
            "increment_feet": {"<Button-1>": self.increment_feet},
            "decrement_feet": {"<Button-1>": self.decrement_feet},
            "increment_inches": {"<Button-1>": self.increment_inches},
            "decrement_inches": {"<Button-1>": self.decrement_inches},
        }

        for tag, events in binds.items():
            canvas = self.weight_canvas if "weight" in tag else self.height_canvas

            for event, callback in events.items():
                canvas.tag_bind(tag, event, callback)

            canvas.tag_bind(tag, "<Enter>", lambda e, t=tag: self.hover_enter(e, t))
            canvas.tag_bind(tag, "<Leave>", lambda e, t=tag: self.hover_leave(e, t))

        self.update_bmi()
        self.window.mainloop()

    def increment_weight(self, event):
        self.weight += 1
        self.update_bmi()

    def decrement_weight(self, event):
        self.weight -= 1 if self.weight > 0 else 0
        self.update_bmi()

    def increment_weight5(self, event):
        self.weight += 5
        self.update_bmi()

    def decrement_weight5(self, event):
        self.weight -= 5 if self.weight > 0 else 0
        self.update_bmi()

    def increment_feet(self, event):
        if self.height_feet < 10:
            self.height_feet += 1
        self.update_bmi()

    def decrement_feet(self, event):
        if self.height_feet > 1:
            self.height_feet -= 1
        elif self.height_feet == 0 and self.height_inches > 0:
            self.height_inches -= 1
        self.update_bmi()

    def increment_inches(self, event):
        self.height_inches += 1
        if self.height_inches >= 12:
            self.height_inches = 0
            if self.height_feet < 10:
                self.height_feet += 1
        self.update_bmi()

    def decrement_inches(self, event):
        if self.height_inches > 0:
            self.height_inches -= 1
        elif self.height_inches == 0 and self.height_feet > 0:
            self.height_feet -= 1
            self.height_inches = 11
        self.update_bmi()

    def update_bmi(self):
        bmi = calculate_bmi(self.weight, self.height_feet, self.height_inches)
        category = get_bmi_category(bmi)

        color_map = {
            "UNDERWEIGHT": "#59C2AD",
            "NORMAL": "#64BA46",
            "OVERWEIGHT": "#FAA727",
            "OBESE": "#F36D27",
        }

        self.bmi_color = color_map.get(category, "#64BA46")
        self.result_canvas.itemconfig("bmi_rectangle", fill=self.bmi_color)

        self.weight_canvas.itemconfig(self.weight_text, text=str(self.weight))
        self.height_canvas.itemconfig(self.feet_text, text=str(self.height_feet))
        self.height_canvas.itemconfig(self.inches_text, text=str(self.height_inches))

        self.result_canvas.itemconfig(self.bmi_text, text=str(round(bmi, 1)))
        self.result_canvas.itemconfig(self.category_text, text=category)

    def hover_enter(self, event, tag):
        if "weight" in tag:
            self.weight_canvas.itemconfig(tag, fill="#576574")
            self.weight_canvas.itemconfig("text", fill="#fff")
        else:
            self.height_canvas.itemconfig(tag, fill="#576574")
            self.height_canvas.itemconfig("text", fill="#fff")

    def hover_leave(self, event, tag):
        if "weight" in tag:
            self.weight_canvas.itemconfig(tag, fill="#273c75")
            self.weight_canvas.itemconfig("text", fill="#fff")
        else:
            self.height_canvas.itemconfig(tag, fill="#273c75")
            self.height_canvas.itemconfig("text", fill="#fff")
