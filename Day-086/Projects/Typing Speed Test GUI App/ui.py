from tkinter import Tk, Canvas, Entry
from text_manager import TextManager
from timer import Timer


class UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed Test")

        self.header_canvas = Canvas(
            self.window, width=800, height=100, highlightthickness=0
        )
        self.header_canvas.pack(fill="x")
        self.header_canvas.create_text(
            400, 50, text="Typing Speed Test", font=("TkFixedFont", 32, "bold")
        )

        self.display_canvas = Canvas(
            self.window, width=800, height=200, highlightthickness=0
        )
        self.display_canvas.pack(fill="x")

        self.text_manager = TextManager(self.display_canvas)
        self.text_manager.display_shuffled_text()

        self.typing_entry = Entry(self.window, font=("TkFixedFont", 24))
        self.typing_entry.pack(fill="x", padx=10, pady=10)
        self.typing_entry.bind("<KeyRelease>", self.on_key_release)

        self.timer = Timer(self.window)

        self.window.mainloop()

    def on_key_release(self, event):
        typed_text = self.typing_entry.get()
        self.text_manager.update_displayed_text_color(typed_text)
