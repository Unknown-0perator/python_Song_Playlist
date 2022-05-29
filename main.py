from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

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

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope='playlist-modify-private',
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri='Your redirect_uri from Spotify',
        show_dialog=True,
        cache_path='Token.txt'
    )
)
user_id = sp.current_user()['id']
