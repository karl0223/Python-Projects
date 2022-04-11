import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

top_movies_web = response.text

soup = BeautifulSoup(top_movies_web, "html.parser")

movie_titles = soup.find_all("h3", class_="title")

title_list = [title.getText() for title in movie_titles]

reversed_list = []

for i in range (len(title_list)):
    last_item = title_list.pop()
    reversed_list.append(last_item)

with open("movies.txt", "w", encoding="utf-8") as file:
    for item in reversed_list:
        file.write(item + "\n")





