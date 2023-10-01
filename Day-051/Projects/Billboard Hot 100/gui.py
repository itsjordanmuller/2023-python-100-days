from tkinter import *


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Billboard Hot 100 Playlist Creator")

        self.title_label = Label(text="Billboard Hot 100")
        self.title_label.grid(column=0, row=0, columnspan=2)

        self.year_label = Label(text="Year: ")
        self.year_label.grid(column=0, row=1)

        self.year_entry = Entry()
        self.year_entry.grid(column=1, row=1)

        self.month_label = Label(text="Month: ")
        self.month_label.grid(column=0, row=2)

        self.month_entry = Entry()
        self.month_entry.grid(column=1, row=2)

        self.day_label = Label(text="Day: ")
        self.day_label.grid(column=0, row=3)

        self.day_entry = Entry()
        self.day_entry.grid(column=1, row=3)

        self.window.mainloop()
