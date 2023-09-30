from tkinter import *
from tkcalendar import Calendar
from datetime import datetime
import json
import random


class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Billboard Top 100 Playlist Creator")
        self.window.config(width=700, height=500)

        self.window.grid_columnconfigure(0, minsize=350)
        self.window.grid_columnconfigure(1, minsize=350)

        self.header_canvas = Canvas(
            self.window, height=100, width=700, bg="#E20A17", highlightthickness=0
        )
        self.header_canvas.grid(row=0, columnspan=2)

        self.logo = PhotoImage(file="./images/BillboardHot100Logo.png").subsample(
            x=4, y=4
        )
        self.header_canvas.create_image(10, 50, anchor=W, image=self.logo)
        self.header_canvas.create_text(
            420, 50, text="Billboard Hot 100", font=("TkFixedFont", 40, "bold")
        )

        self.calendar_canvas = Canvas(
            self.window, height=400, width=350, bg="#0082D6", highlightthickness=0
        )
        self.calendar_canvas.grid(column=0, row=1)

        self.instructions_label = Label(
            self.calendar_canvas,
            text="PICK A DATE",
            bg="#FFF100",
            fg="black",
            font=("TkFixedFont", 20, "bold"),
        )
        self.instructions_label.grid(row=0, column=0, sticky=EW)

        today = datetime.today()

        self.calendar = Calendar(
            self.calendar_canvas,
            selectmode="day",
            year=today.year,
            month=today.month,
            day=today.day,
        )
        self.calendar.grid(row=1, column=0)

        self.selected_date_label = Label(
            self.calendar_canvas,
            text="",
            bg="#0082D6",
            fg="white",
            font=("TkFixedFont", 24, "bold"),
        )
        self.update_selected_date_label()
        self.selected_date_label.grid(row=2, column=0)

        self.calendar.bind("<<CalendarSelected>>", self.on_date_selected)

        self.control_canvas = Canvas(
            self.window, height=400, width=350, bg="#FFFFFF", highlightthickness=0
        )
        self.control_canvas.grid(column=1, row=1)
        self.control_canvas.grid_propagate(False)

        for i in range(2):
            self.control_canvas.grid_rowconfigure(i, weight=1)

        self.control_canvas.grid_columnconfigure(0, weight=1)

        self.search_button = Button(
            self.control_canvas,
            text="Search Songs",
            command=self.search,
            bg="#E20A17",
            fg="white",
            font=("TkFixedFont", 16, "bold"),
        )
        self.search_button.grid(column=0, row=0)

        self.another_button = Button(
            self.control_canvas,
            text="Create Playlist",
            command=self.search,
            bg="green",
            fg="white",
            font=("TkFixedFont", 16, "bold"),
        )
        self.another_button.grid(column=0, row=1)

        # self.yet_another_button = Button(
        #     self.control_canvas,
        #     text="Another Button",
        #     command=self.search,
        #     bg="green",
        #     fg="white",
        #     font=("TkFixedFont", 16, "bold"),
        # )
        # self.yet_another_button.grid(column=0, row=2)

        self.window.mainloop()

    def on_date_selected(self, event):
        self.update_selected_date_label()

    def update_selected_date_label(self):
        selected_date = self.calendar.get_date()
        self.selected_date_label.config(text=f"{selected_date}")

    def search(self):
        selected_date = self.calendar.get_date()
        print("Searching for Songs, Please Wait...")
