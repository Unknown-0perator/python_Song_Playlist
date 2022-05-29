from bs4 import BeautifulSoup
import requests


CLIENT_ID = 'Your Spotify Client_ID'
CLIENT_SECRET = 'Your Spotify Client_Secret'

date_input = input('what year you would like to travel to in (YYY-MM-DD format): ')
end_point = f'https://www.billboard.com/charts/hot-100/{date_input}'
print(end_point)
response = requests.get(url=end_point)
billboard = response.text
soup = BeautifulSoup(billboard, 'html.parser')
song_list = [song.getText().strip() for song in soup.findAll(name='h3', class_='a-no-trucate')]
print(song_list)
