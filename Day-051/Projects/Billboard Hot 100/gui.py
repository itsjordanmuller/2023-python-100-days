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

        self.date_select_button = Button(text="Search Date", command=self.search_date)
        self.date_select_button.grid(column=0, row=4, columnspan=2)

        self.date_select_status = Label(text="")
        self.date_select_status.grid(column=0, row=5, columnspan=2)

        self.search_songs_button = Button(
            text="Search Songs", command=self.search_songs
        )
        self.search_songs_button.grid(column=0, row=6, columnspan=2)

        self.search_songs_status = Label(text="")
        self.search_songs_status.grid(column=0, row=7, columnspan=2)

        self.create_playlist_button = Button(
            text="Create Playlist", command=self.create_playlist
        )
        self.create_playlist_button.grid(column=0, row=8, columnspan=2)

        self.create_playlist_status = Label(text="")
        self.create_playlist_status.grid(column=0, row=9, columnspan=2)

        self.window.mainloop()

    def search_date(self):
        self.date_select_status.config(text="Date Set", fg="green")

    def search_songs(self):
        self.search_songs_status.config(text="Searching...", fg="orange")

    def create_playlist(self):
        self.create_playlist_status.config(text="Playlist Created", fg="green")
