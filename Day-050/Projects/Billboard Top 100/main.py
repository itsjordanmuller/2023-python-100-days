import os
import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from ui import UserInterface

ui = UserInterface()

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

BASE_DIR = "./scraped_data/"

if not os.path.exists(BASE_DIR):
    os.mkdir(BASE_DIR)


def extract_date_from_url(url):
    return url.split("/")[-2]


def save_scraped_data(date_string, content, file_type="html"):
    with open(
        os.path.join(BASE_DIR, f"{date_string}.{file_type}"), "w", encoding="utf-8"
    ) as file:
        if file_type == "json":
            json.dump(content, file, ensure_ascii=False, indent=4)
        else:
            file.write(content)


def load_scraped_data(date_string, file_type="html"):
    with open(
        os.path.join(BASE_DIR, f"{date_string}.{file_type}"), "r", encoding="utf-8"
    ) as file:
        if file_type == "json":
            return json.load(file)
        else:
            return file.read()


year = input("Enter the year (e.g. 1999): ")
month = input("Enter the month (01-12): ")
day = input("Enter the day (01-31): ")

url = f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/"
date_string = extract_date_from_url(url)

if f"{date_string}.html" in os.listdir(BASE_DIR):
    user_input = input(
        f"Data for {date_string} has been scraped before. Do you want to scrape it again? (yes/no): "
    )
    if user_input != "yes":
        content = load_scraped_data(date_string)
else:
    response = requests.get(url)
    content = response.text
    save_scraped_data(date_string, content)

soup = BeautifulSoup(content, "html.parser")

all_songs = soup.select(selector="li h3#title-of-a-story")
all_artists = soup.select(selector="span.a-font-primary-s.a-no-trucate")

songs_data = []
place = 1

for song, artist in zip(all_songs, all_artists):
    song_details = {
        "place": place,
        "song": song.getText().strip(),
        "artist": artist.getText().strip(),
    }
    songs_data.append(song_details)
    place += 1

save_scraped_data(date_string, songs_data, "json")

# print(songs_data)
# print(len(songs_data))
print("Searching for Songs, Please Wait...")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://localhost:8080/callback",
        scope="playlist-modify-private",
    )
)


def search_track(song, artist):
    query = f"{song} {artist}"
    result = sp.search(query, type="track", limit=1)
    tracks = result.get("tracks", {}).get("items", [])
    return tracks[0].get("id") if tracks else None


track_ids = []
for song_data in songs_data:
    track_id = search_track(song_data["song"], song_data["artist"])
    if track_id:
        track_ids.append(track_id)


def create_playlist(user_id, playlist_name):
    playlist = sp.user_playlist_create(user_id, playlist_name, public=False)
    return playlist["id"]


user_confirmation = input(
    "Would you like to create the playlist on Spotify? (yes/no): "
)

if user_confirmation.lower() == "yes":
    user = sp.current_user()
    playlist_id = create_playlist(user["id"], f"Billboard Top 100 - {date_string}")

    def add_tracks_to_playlist(playlist_id, track_ids):
        sp.playlist_add_items(playlist_id, track_ids)

    add_tracks_to_playlist(playlist_id, track_ids)
else:
    print("Playlist creation aborted.")
