import csv

import requests
from bs4 import BeautifulSoup


def scrape():
    response = requests.get("https://realpython.github.io/fake-jobs/")
    html = BeautifulSoup(response.text, "html.parser")

    cards = html.select(".card-content")
    data = [("JOB_TITLE", "COMPANY", "LOCATION", "URL")]

    for card in cards:
        data.append(
            (
                card.select(".title")[0].text.strip(),
                card.select(".company")[0].text.strip(),
                card.select(".location")[0].text.strip(),
                card.select("a:last-child")[0]["href"].strip(),
            )
        )

    print(data)

    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    scrape()
