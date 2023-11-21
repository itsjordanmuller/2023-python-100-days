from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
)

empire_100_movies = response.text

soup = BeautifulSoup(empire_100_movies, "html.parser")

all_movies = soup.select(selector=".article-title-description__text .title")

movie_texts = []

for movie in all_movies:
    movie_text = movie.getText()
    movie_texts.append(movie_text)
    with open("movies.txt", "a") as f:
        f.write(movie_text + "\n")

with open("movies.txt", "r") as f:
    movies = f.readlines()

reordered_movies = movies[::-1]

with open("reordered_movies.txt", "w") as f:
    for movie in reordered_movies:
        f.write(movie)
