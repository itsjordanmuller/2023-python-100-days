import os
from tkinter import *
from tkinter import filedialog, colorchooser
from PIL import Image, ImageTk, ImageDraw, ImageFont


class UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Image Watermarker")
        self.watermark_text = StringVar()
        self.watermark_opacity = DoubleVar(value=1.0)
        self.watermark_position = StringVar(value="bottom right")
        self.watermark_font_size = IntVar(value=1)
        self.watermark_color = StringVar(value="#FFFFFF")
        self.watermarked_image = None

        self.header_canvas = Canvas(
            self.window, width=800, height=50, highlightthickness=0, bg="#bdc3c7"
        )
        self.header_canvas.grid(column=0, row=0)
        self.header_canvas.create_text(
            400, 25, text="Image Watermarker", font=("TkFixedFont", 24, "bold")
        )

        self.image_canvas = Canvas(
            self.window, width=800, height=600, highlightthickness=0, bg="#34495e"
        )
        self.image_canvas.grid(column=0, row=1)

        self.original_image = None
        self.tk_image = None
        self.image_on_canvas = None

        self.controls_canvas = Canvas(
            self.window, width=800, height=100, highlightthickness=0, bg="#7f8c8d"
        )
        self.controls_canvas.grid(column=0, row=2)

        self.first_row_frame = Frame(self.controls_canvas, bg="#7f8c8d")
        self.first_row_frame.pack(anchor="center")

        self.second_row_frame = Frame(self.controls_canvas, bg="#7f8c8d")
        self.second_row_frame.pack(anchor="center")

        self.upload_button = Button(
            self.first_row_frame, text="Upload Image", command=self.upload_image
        )
        self.upload_button.pack(side=LEFT, padx=10)

        self.default_image_button = Button(
            self.first_row_frame,
            text="Load Default Image",
            command=self.load_default_image,
        )
        self.default_image_button.pack(side=LEFT, padx=10)

        self.save_button = Button(
            self.first_row_frame, text="Save Image", command=self.save_watermarked_image
        )
        self.save_button.pack(side=LEFT, padx=10)

        self.zoom_slider = Scale(
            self.first_row_frame,
            from_=10,
            to=200,
            orient=HORIZONTAL,
            label="Zoom",
            resolution=10,
            command=self.update_zoom,
        )
        self.zoom_slider.set(100)
        self.zoom_slider.pack(side=LEFT)

        self.watermark_entry = Entry(
            self.second_row_frame, textvariable=self.watermark_text, width=30
        )
        self.watermark_entry.pack(side=LEFT, padx=10)

        self.opacity_slider = Scale(
            self.second_row_frame,
            from_=0,
            to=100,
            orient=HORIZONTAL,
            label="Opacity",
            resolution=1,
            variable=self.watermark_opacity,
        )
        self.opacity_slider.set(100)
        self.opacity_slider.pack(side=LEFT)

        self.font_size_slider = Scale(
            self.second_row_frame,
            from_=8,
            to=120,
            orient=HORIZONTAL,
            label="Font Size",
            resolution=2,
            variable=self.watermark_font_size,
        )
        self.font_size_slider.set(20)
        self.font_size_slider.pack(side=LEFT)

        self.color_button = Button(
            self.second_row_frame, text="Select Color", command=self.choose_color
        )
        self.color_button.pack(side=LEFT, padx=10)

        self.position_menu = OptionMenu(
            self.second_row_frame,
            self.watermark_position,
            "top left",
            "top right",
            "bottom left",
            "bottom right",
            "center",
        )
        self.position_menu.pack(side=LEFT, padx=10)

        self.apply_watermark_button = Button(
            self.second_row_frame, text="Apply Watermark", command=self.apply_watermark
        )
        self.apply_watermark_button.pack(side=LEFT, padx=10)

        self.load_default_image()
        self.window.mainloop()

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("image files", (".png", ".jpg", ".jpeg", ".gif", ".bmp"))],
        )
        if self.image_path:
            self.set_canvas_loading(True)
            self.original_image = Image.open(self.image_path)

            if self.original_image.mode != "RGBA":
                self.original_image = self.original_image.convert("RGBA")

            self.initial_zoom = self.calculate_initial_zoom()
            self.zoom_slider.set(self.initial_zoom)
            self.display_image(zoom=self.initial_zoom)
            self.watermarked_image = self.original_image.copy()
            self.set_canvas_loading(False)

    def set_canvas_loading(self, loading):
        """Change the canvas background color based on the loading state."""
        color = "#FFA500" if loading else "#34495e"
        self.image_canvas.config(bg=color)
        self.image_canvas.update()

    def calculate_initial_zoom(self):
        canvas_width = self.image_canvas.winfo_width()
        canvas_height = self.image_canvas.winfo_height()

        if canvas_width == 1:
            canvas_width = 800
        if canvas_height == 1:
            canvas_height = 600

        image_width, image_height = self.original_image.size

        width_scale = canvas_width / image_width
        height_scale = canvas_height / image_height

        initial_scale = min(width_scale, height_scale)

        return int(initial_scale * 100)

    def display_image(self, zoom=100):
        if not self.original_image:
            return

        zoom = zoom / 100.0
        image_width, image_height = self.original_image.size
        new_size = (int(image_width * zoom), int(image_height * zoom))

        image_to_display = (
            self.watermarked_image if self.watermarked_image else self.original_image
        )
        resized_image = image_to_display.resize(new_size, Image.Resampling.LANCZOS)

        self.tk_image = ImageTk.PhotoImage(resized_image)

        if self.image_on_canvas:
            self.image_canvas.delete(self.image_on_canvas)

        self.image_on_canvas = self.image_canvas.create_image(
            400, 300, image=self.tk_image
        )

    def update_zoom(self, val):
        if self.original_image:
            self.display_image(zoom=int(val))

    def load_default_image(self):
        default_image_path = "defaultImage.jpg"
        if os.path.isfile(default_image_path):
            self.set_canvas_loading(True)
            self.original_image = Image.open(default_image_path)

            if self.original_image.mode != "RGBA":
                self.original_image = self.original_image.convert("RGBA")

            self.initial_zoom = self.calculate_initial_zoom()
            self.zoom_slider.set(self.initial_zoom)
            self.display_image(zoom=self.initial_zoom)
            self.watermarked_image = self.original_image.copy()
            self.set_canvas_loading(False)
        else:
            print(f"Error: The file '{default_image_path}' does not exist.")
