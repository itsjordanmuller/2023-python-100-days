from tkinter import *


class UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed Test")

        self.header_canvas = Canvas(
            self.window, width=800, height=100, highlightthickness=0
        )
        self.header_canvas.grid(column=0, row=0)
        self.header_canvas.create_text(
            400, 50, text="Typing Speed Test", font=("TkFixedFont", 32, "bold")
        )

        self.display_canvas = Canvas(
            self.window, width=800, height=300, highlightthickness=0
        )
        self.display_canvas.grid(column=0, row=1)

        self.typing_canvas = Canvas(
            self.window, width=800, height=300, highlightthickness=0
        )
        self.typing_canvas.grid(column=0, row=2)

        self.window.mainloop()
