from tkinter import *
from tkcalendar import Calendar
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
        self.header_canvas.grid(column=0, row=0, columnspan=2)

        self.logo = PhotoImage(file="./images/BillboardHot100Logo.png").subsample(
            x=4, y=4
        )
        self.header_canvas.create_image(10, 50, anchor=W, image=self.logo)
        self.header_canvas.create_text(
            420, 50, text="Billboard Hot 100", font=("TkFixedFont", 40, "bold")
        )

        self.date_canvas = Canvas(
            width=350, height=400, bg="#FFFFFF", highlightthickness=0
        )
        self.date_canvas.grid(column=1, row=1)

        self.calendar_canvas = Canvas(
            width=350, height=400, bg="#0082D6", highlightthickness=0
        )
        self.calendar_canvas.grid(column=0, row=1)

        self.calendar = Calendar(
            self.window,
            selectmode="day",
            year=2023,
            month=9,
            day=30,
            width=350,
            height=400,
        )

        self.calendar_window = self.calendar_canvas.create_window(
            50, 50, anchor=NW, window=self.calendar
        )

        self.window.mainloop()
