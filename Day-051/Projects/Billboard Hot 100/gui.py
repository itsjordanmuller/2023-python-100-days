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

        self.window.mainloop()
