import os
import json
from tkinter import *
from tkinter import messagebox
from scrape import Scraper, BASE_DIR
from tkcalendar import Calendar
from datetime import datetime


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Billboard Hot 100 Playlist Creator")

        self.today = datetime.today()

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

        self.selected_date_label = Label(
            self.date_canvas,
            text=self.today.strftime("%m/%d/%Y"),
            font=("TkFixedFont", 32, "bold"),
        )
        self.selected_date_label_window = self.date_canvas.create_window(
            150, 65, window=self.selected_date_label
        )

        self.year_label = Label(self.date_canvas, text="Year: ", width=7)
        self.year_label_window = self.date_canvas.create_window(
            100, 120, window=self.year_label
        )

        self.year_entry = Entry(self.date_canvas, width=10)
        self.year_entry_window = self.date_canvas.create_window(
            185, 120, window=self.year_entry
        )

        self.month_label = Label(self.date_canvas, text="Month: ", width=7)
        self.month_label_window = self.date_canvas.create_window(
            100, 150, window=self.month_label
        )

        self.month_entry = Entry(self.date_canvas, width=10)
        self.month_entry_window = self.date_canvas.create_window(
            185, 150, window=self.month_entry
        )

        self.day_label = Label(self.date_canvas, text="Day: ", width=7)
        self.day_label_window = self.date_canvas.create_window(
            100, 180, window=self.day_label
        )

        self.day_entry = Entry(self.date_canvas, width=10)
        self.day_entry_window = self.date_canvas.create_window(
            185, 180, window=self.day_entry
        )

        self.calendar = Calendar(
            self.date_canvas,
            selectmode="day",
            year=self.today.year,
            month=self.today.month,
            day=self.today.day,
        )
        self.calendar_window = self.date_canvas.create_window(
            150, 285, window=self.calendar
        )

        self.formatted_date = self.today.strftime("%m/%d/%Y")
        self.selected_date_label.config(text=self.formatted_date)

        self.year_entry.insert(0, self.today.year)
        self.month_entry.insert(0, self.today.strftime("%m"))
        self.day_entry.insert(0, self.today.strftime("%d"))

        self.calendar.bind("<<CalendarSelected>>", self.update_date)

        self.year_entry.bind("<KeyRelease>", self.entry_updated)
        self.month_entry.bind("<KeyRelease>", self.entry_updated)
        self.day_entry.bind("<KeyRelease>", self.entry_updated)

        self.button_canvas = Canvas(
            self.window, width=300, height=400, bg="#FFF100", highlightthickness=0
        )
        self.button_canvas.grid(column=1, row=1)
        self.button_canvas.create_rectangle(25, 25, 275, 375, fill="#fff", width=0)

        self.date_select_button = Button(
            self.button_canvas, text="Search Date", command=self.search_date
        )
        self.date_select_button_window = self.button_canvas.create_window(
            150, 85, window=self.date_select_button
        )

        self.date_select_status = Label(self.button_canvas, text="", bg="#fff")
        self.date_select_status_window = self.button_canvas.create_window(
            150, 115, window=self.date_select_status
        )

        self.search_songs_button = Button(
            self.button_canvas, text="Search Songs", command=self.search_songs
        )
        self.search_songs_button_window = self.button_canvas.create_window(
            150, 185, window=self.search_songs_button
        )

        self.search_songs_status = Label(self.button_canvas, text="", bg="#fff")
        self.search_songs_status_window = self.button_canvas.create_window(
            150, 215, window=self.search_songs_status
        )

        self.create_playlist_button = Button(
            self.button_canvas, text="Create Playlist", command=self.create_playlist
        )
        self.create_playlist_button_window = self.button_canvas.create_window(
            150, 285, window=self.create_playlist_button
        )

        self.create_playlist_status = Label(self.button_canvas, text="", bg="#fff")
        self.create_playlist_status_window = self.button_canvas.create_window(
            150, 315, window=self.create_playlist_status
        )

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

        self.search_songs_status.config(text="Songs found", fg="green")

    def create_playlist(self):
        year = self.year_entry.get()
        month = self.month_entry.get()
        day = self.day_entry.get()

        self.scraper = Scraper(year, month, day)
        songs = self.scraper.scrape()
        self.create_playlist_status.config(text="Creating playlist...", fg="orange")
        playlist_url = self.scraper.create_playlist()
        self.create_playlist_status.config(text=f"Playlist Created", fg="green")

    def update_date(self, event):
        date = self.calendar.get_date()
        month, day, year = map(int, date.split("/"))

        pivot_year = 25

        if year <= pivot_year:
            year += 2000
        else:
            year += 1900

        formatted_date = f"{month:02d}/{day:02d}/{year}"
        self.selected_date_label.config(text=formatted_date)

        self.year_entry.delete(0, END)
        self.year_entry.insert(0, year)

        self.month_entry.delete(0, END)
        self.month_entry.insert(0, f"{month:02d}")

        self.day_entry.delete(0, END)
        self.day_entry.insert(0, f"{day:02d}")

    def entry_updated(self, event):
        try:
            year = int(self.year_entry.get(), 10)
            month = int(self.month_entry.get(), 10)
            day = int(self.day_entry.get(), 10)
            new_date = datetime(year, month, day).date()
            self.calendar.selection_set(new_date)
            self.selected_date_label.config(text=f"{month:02d}/{day:02d}/{year}")
        except ValueError as ve:
            print(f"ValueError: {ve}")
        except Exception as e:
            print(f"Exception: {e}")
