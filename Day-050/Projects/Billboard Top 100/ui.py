from tkinter import *
import json
import random


class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Billboard Top 100 Playlist Creator")
        self.window.config(width=700, height=500)

        self.header_canvas = Canvas(
            width=700, height=100, bg="#E20A17", highlightthickness=0
        )
        self.header_canvas.grid(column=0, row=0)

        self.logo = PhotoImage(file="./images/BillboardHot100Logo.png").subsample(
            x=4, y=4
        )
        self.header_canvas.create_image(10, 50, anchor=W, image=self.logo)
        self.header_canvas.create_text(
            420, 50, text="Billboard Hot 100", font=("TkFixedFont", 40, "bold")
        )

        self.control_canvas = Canvas(
            width=700, height=400, bg="#0082D6", highlightthickness=0
        )
        self.control_canvas.grid(column=0, row=1)

        self.window.mainloop()
