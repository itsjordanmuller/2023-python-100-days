from tkinter import *
from tkinter import Tk, Canvas, filedialog, Scale
from PIL import Image, ImageTk


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

        self.first_row_frame = Frame(self.controls_canvas, bg="#7f8c8d")
        self.first_row_frame.pack(anchor="center")

        self.second_row_frame = Frame(self.controls_canvas, bg="#7f8c8d")
        self.second_row_frame.pack(anchor="center")

        self.upload_button = Button(
            self.first_row_frame, text="Upload Image", command=self.upload_image
        )
        self.upload_button.pack(side=LEFT, padx=10)

        self.zoom_slider = Scale(
            self.controls_canvas,
            from_=10,
            to=200,
            orient=HORIZONTAL,
            label="Zoom",
            command=self.update_zoom,
        )
        self.zoom_slider.pack()

        self.window.mainloop()

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("image files", (".png", ".jpg", ".jpeg", ".gif", ".bmp"))],
        )
        if self.image_path:
            self.original_image = Image.open(self.image_path)
            self.display_image()

    def display_image(self):
        self.tk_image = ImageTk.PhotoImage(self.original_image)
        self.image_canvas.create_image(400, 300, image=self.tk_image)

    def update_zoom(self, val):
        zoom = int(val) / 100.0
        width, height = self.original_image.size
        new_size = (int(width * zoom), int(height * zoom))
        resized_image = self.original_image.resize(new_size, Image.ANTIALIAS)
        self.display_image(resized_image)

    def display_image(self, image=None):
        if image is None:
            image = self.original_image
        self.tk_image = ImageTk.PhotoImage(image)
        self.image_canvas.create_image(400, 300, image=self.tk_image)
