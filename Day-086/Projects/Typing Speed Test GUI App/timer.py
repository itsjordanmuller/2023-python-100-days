from tkinter import Canvas
import time


class Timer:
    def __init__(self, window, width=800, height=150):
        self.window = window
        self.timer_canvas = Canvas(
            window, width=width, height=height, highlightthickness=0
        )
        self.timer_canvas.pack(fill="x")
        self.timer_text = self.timer_canvas.create_text(
            width // 2, height // 2, text="00:00", font=("TkFixedFont", 32, "bold")
        )
        self.start_time = None

    def start_timer(self):
        self.start_time = time.time()
        self.update_timer()

    def update_timer(self):
        if self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            minutes, seconds = divmod(int(elapsed_time), 60)
            time_str = f"{minutes:02d}:{seconds:02d}"
            self.timer_canvas.itemconfig(self.timer_text, text=time_str)
            self.window.after(1000, self.update_timer)

    def stop_timer(self):
        self.start_time = None
