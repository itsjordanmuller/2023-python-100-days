import os
import json
from tkinter import *
from tkinter import messagebox
from scrape import Scraper, BASE_DIR


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Billboard Hot 100 Playlist Creator")

        self.header_canvas = Canvas(
            self.window, width=600, height=100, bg="#E20A17", highlightthickness=0
        )
        self.header_canvas.grid(column=0, row=0, columnspan=2)

        self.logo = PhotoImage(file="./images/BillboardHot100Logo.png").subsample(
            x=4, y=4
        )
        self.header_canvas.create_image(10, 50, anchor=W, image=self.logo)
        self.header_canvas.create_text(
            590,
            50,
            anchor=E,
            text="Billboard Hot 100",
            font=("TkFixedFont", 36, "bold"),
        )

        # self.title_label = Label(text="Billboard Hot 100")
        # self.title_label.grid(column=0, row=0, columnspan=2, pady=15)

        self.date_canvas = Canvas(
            self.window, width=300, height=400, bg="#0082D6", highlightthickness=0
        )
        self.date_canvas.grid(column=0, row=1)
        self.date_canvas.create_rectangle(25, 25, 275, 375, fill="#fff", width=0)

        self.year_label = Label(self.date_canvas, text="Year: ", width=7)
        self.year_label_window = self.date_canvas.create_window(
            100, 100, window=self.year_label
        )

        self.year_entry = Entry(self.date_canvas, width=10)
        self.year_entry_window = self.date_canvas.create_window(
            185, 100, window=self.year_entry
        )

        self.month_label = Label(self.date_canvas, text="Month: ", width=7)
        self.month_label_window = self.date_canvas.create_window(
            100, 130, window=self.month_label
        )

        self.month_entry = Entry(self.date_canvas, width=10)
        self.month_entry_window = self.date_canvas.create_window(
            185, 130, window=self.month_entry
        )

        self.day_label = Label(self.date_canvas, text="Day: ", width=7)
        self.day_label_window = self.date_canvas.create_window(
            100, 160, window=self.day_label
        )

        self.day_entry = Entry(self.date_canvas, width=10)
        self.day_entry_window = self.date_canvas.create_window(
            185, 160, window=self.day_entry
        )

        self.button_canvas = Canvas(
            self.window, width=300, height=400, bg="#FFF100", highlightthickness=0
        )
        self.button_canvas.grid(column=1, row=1)
        self.button_canvas.create_rectangle(25, 25, 275, 375, fill="#fff", width=0)

        # self.date_select_button = Button(text="Search Date", command=self.search_date)
        # self.date_select_button.grid(column=0, row=4, columnspan=2)

        # self.date_select_status = Label(text="")
        # self.date_select_status.grid(column=0, row=5, columnspan=2)

        # self.search_songs_button = Button(
        #     text="Search Songs", command=self.search_songs
        # )
        # self.search_songs_button.grid(column=0, row=6, columnspan=2)

        # self.search_songs_status = Label(text="")
        # self.search_songs_status.grid(column=0, row=7, columnspan=2)

        # self.create_playlist_button = Button(
        #     text="Create Playlist", command=self.create_playlist
        # )
        # self.create_playlist_button.grid(column=0, row=8, columnspan=2)

        # self.create_playlist_status = Label(text="")
        # self.create_playlist_status.grid(column=0, row=9, columnspan=2)

        self.window.mainloop()

    def search_date(self):
        year = self.year_entry.get()
        month = self.month_entry.get()
        day = self.day_entry.get()
        print(year, month, day)
        self.date_select_status.config(text="Date Set", fg="green")

    def search_songs(self):
        year = self.year_entry.get()
        month = self.month_entry.get()
        day = self.day_entry.get()
        file_path = os.path.join(BASE_DIR, f"{year}-{month}-{day}.json")

        if os.path.exists(file_path):
            use_existing_data = messagebox.askyesno(
                "Data Exists",
                "Data for this date already exists. Do you want to use the existing data?",
            )
            if use_existing_data:
                with open(file_path, "r", encoding="utf-8") as file:
                    self.songs_data = json.load(file)
                self.search_songs_status.config(
                    text=f"{len(self.songs_data)} songs in existing data",
                    fg="green",
                )
                return

        self.search_songs_status.config(text="Searching for songs...", fg="orange")

        self.scraper = Scraper(year, month, day)
        songs = self.scraper.scrape()

        self.search_songs_status.config(text=f"{len(songs)} songs found", fg="green")

    def create_playlist(self):
        self.create_playlist_status.config(text="Creating playlist...", fg="orange")
        playlist_url = self.scraper.create_playlist()
        self.create_playlist_status.config(text=f"Playlist Created", fg="green")
