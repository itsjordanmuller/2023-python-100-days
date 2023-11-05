from tkinter import Tk, Canvas, Entry, Button
from text_manager import TextManager
from timer import Timer
import time


class UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed Test")

        self.header_canvas = Canvas(
            self.window, width=600, height=100, highlightthickness=0
        )
        self.header_canvas.pack(fill="x")
        self.header_text = self.header_canvas.create_text(
            300, 50, text="Typing Speed Test", font=("TkFixedFont", 32, "bold")
        )

        self.display_canvas = Canvas(
            self.window, width=600, height=200, highlightthickness=0
        )
        self.display_canvas.pack(fill="x")

        self.text_manager = TextManager(self.display_canvas)

        self.typing_entry = Entry(self.window, font=("TkFixedFont", 24))
        self.typing_entry.pack(fill="x", padx=10, pady=10)
        self.typing_entry.bind("<KeyRelease>", self.on_key_release)

        self.timer = Timer(self.window)

        self.start_button = Button(self.window, text="Start", command=self.start_test)
        self.start_button.pack(pady=20)

        self.window.mainloop()

    def start_test(self):
        self.start_button.config(state="disabled")
        self.countdown(3)

    def countdown(self, count):
        if count > 0:
            self.header_canvas.itemconfig(self.header_text, text=str(count))
            self.window.after(1000, self.countdown, count - 1)
        else:
            self.header_canvas.itemconfig(self.header_text, text="Go!")
            self.text_manager.display_shuffled_text()
            self.timer.start_timer()
            self.typing_entry.focus_set()

    def on_key_release(self, event):
        typed_text = self.typing_entry.get()
        self.text_manager.update_displayed_text_color(typed_text)
        if typed_text == self.text_manager.shuffled_text:
            self.timer.stop_timer()
            self.header_canvas.itemconfig(self.header_text, text="Finished!")
