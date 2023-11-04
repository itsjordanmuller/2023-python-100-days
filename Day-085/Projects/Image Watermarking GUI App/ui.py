from tkinter import Tk, Canvas


class UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Image Watermarker")

        self.header_canvas = Canvas(self.window, width=800, height=50, bg="#bdc3c7")
        self.header_canvas.grid(column=0, row=0)
        self.header_canvas.create_text(
            400, 25, text="Image Watermarker", font=("TkFixedFont", 24, "bold")
        )

        self.image_canvas = Canvas(self.window, width=800, height=600, bg="#34495e")
        self.image_canvas.grid(column=0, row=1)

        self.controls_canvas = Canvas(self.window, width=800, height=100, bg="#7f8c8d")
        self.controls_canvas.grid(column=0, row=2)

        self.window.mainloop()


if __name__ == "__main__":
    ui = UI()
