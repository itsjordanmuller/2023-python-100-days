import requests
from bs4 import BeautifulSoup

r = requests.get(
    "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
)

print(r)
