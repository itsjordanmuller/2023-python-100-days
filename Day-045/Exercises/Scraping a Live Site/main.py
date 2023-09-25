from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

all_anchor_tags = soup.select(selector=".titleline > a")

article_texts = []
article_links = []

for tag in all_anchor_tags:
    article_text = tag.getText()
    article_texts.append(article_text)
    article_link = tag.get("href")
    article_links.append(article_link)

print(article_texts)
print(article_links)
