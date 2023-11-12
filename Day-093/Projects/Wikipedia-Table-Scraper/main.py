import csv
import requests
from bs4 import BeautifulSoup


def extract_table_data(table):
    caption = table.find("caption")
    caption_text = [caption.get_text(strip=True)] if caption else ["No Caption"]

    rows = table.find_all("tr")
    table_data = [caption_text, []]
    for row in rows:
        cells = row.find_all(["th", "td"])
        cells_text = [cell.get_text(strip=True) for cell in cells]
        table_data.append(cells_text)
    return table_data


def save_to_csv(data, filename):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


def scrape_and_save_tables(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    tables = soup.find_all("table")
    for index, table in enumerate(tables):
        table_data = extract_table_data(table)
        filename = f"table_{index}.csv"
        save_to_csv(table_data, filename)
        print(f"Saved {filename}")


if __name__ == "__main__":
    print("Enter the URL of the Wikipedia page to scrape:")
    url = input().strip()
    scrape_and_save_tables(url)
