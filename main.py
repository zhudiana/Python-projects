from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = "https://www.billboard.com/charts/hot-100/"
response = requests.get(URL + date)

soup = BeautifulSoup(response.text, "html.parser")
song_titles = soup.select(selector="li ul li h3")
song_list = [song.getText().strip() for song in song_titles ]
print(song_list)