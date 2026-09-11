import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36 Edg/152.0.0.0"
}

response = requests.get(url, headers=headers)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")
movie_items = soup.find_all("div", class_="item")

for item in movie_items:
    title_span = item.find("span", class_="title")
    if title_span:
        print(title_span.text)
        