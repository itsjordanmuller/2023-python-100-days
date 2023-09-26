import os
import requests
import json
from bs4 import BeautifulSoup

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

print(songs_data)
print(len(songs_data))
