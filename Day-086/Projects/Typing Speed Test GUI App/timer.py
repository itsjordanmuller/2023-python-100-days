from tkinter import Canvas


class Timer:
    def __init__(self, window, width=800, height=150):
        self.timer_canvas = Canvas(
            window, width=width, height=height, highlightthickness=0
        )
        self.timer_canvas.pack(fill="x")
        self.timer_text = self.timer_canvas.create_text(
            width // 2, height // 2, text="00:00", font=("TkFixedFont", 32, "bold")
        )
