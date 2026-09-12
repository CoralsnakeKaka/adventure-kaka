import requests
from bs4 import BeautifulSoup
import time

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36 Edg/152.0.0.0"
}

total = []
for page in range(0, 10):
    page_url = f"{url}?start={page * 25}"
    response = requests.get(page_url, headers=headers)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")
    movie_items = soup.find_all("div", class_="item")

    for item in movie_items:
        title_span = item.find("span", class_="title")
        if title_span:
            total.append(title_span.text)

    time.sleep(2)
    print("page",page+1,"state",response.status_code)
    print("Total movies found:", len(total))

print(total)