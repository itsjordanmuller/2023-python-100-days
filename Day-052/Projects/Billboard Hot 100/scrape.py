import os
import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

BASE_DIR = "./scraped_data/"

if not os.path.exists(BASE_DIR):
    os.mkdir(BASE_DIR)


class Scraper:
    def __init__(self, year, month, day):
        self.url = f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/"
        self.date_string = f"{year}-{month}-{day}"
        self.songs_data = []
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                redirect_uri="http://localhost:8080/callback",
                scope="playlist-modify-private",
            )
        )

    def scrape(self):
        file_path = os.path.join(BASE_DIR, f"{self.date_string}.html")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
        else:
            response = requests.get(self.url)
            content = response.text
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)

        soup = BeautifulSoup(content, "html.parser")
        all_songs = soup.select(selector="li h3#title-of-a-story")
        all_artists = soup.select(selector="span.a-font-primary-s.a-no-trucate")

        for place, (song, artist) in enumerate(zip(all_songs, all_artists), start=1):
            song_details = {
                "place": place,
                "song": song.text.strip(),
                "artist": artist.text.strip(),
            }
            self.songs_data.append(song_details)

        with open(
            os.path.join(BASE_DIR, f"{self.date_string}.json"), "w", encoding="utf-8"
        ) as file:
            json.dump(self.songs_data, file, ensure_ascii=False, indent=4)

        return self.songs_data

    def create_playlist(self):
        track_ids = [
            self.search_track(song["song"], song["artist"]) for song in self.songs_data
        ]
        track_ids = [tid for tid in track_ids if tid]

        user = self.sp.current_user()
        playlist = self.sp.user_playlist_create(
            user["id"], f"Billboard Top 100 - {self.date_string}", public=False
        )
        self.sp.playlist_add_items(playlist["id"], track_ids)

        return playlist["external_urls"]["spotify"]

    def search_track(self, song, artist):
        query = f"{song} {artist}"
        result = self.sp.search(query, type="track", limit=1)
        tracks = result.get("tracks", {}).get("items", [])
        return tracks[0].get("id") if tracks else None
