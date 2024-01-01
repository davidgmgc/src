import spotipy
from spotipy.oauth2 import SpotifyOAuth

__secret_file = 'secret.json'

def __load_secret(self):
        with open(Auth.__secret_file, 'r') as file:
            secret = json.load(file)

        return secret.get('client_id',''), secret.get('client_secret','')

self.__client_id, self.__client_secret = self.__load_secret()

print (self.__client_id, self.__client_secret)


# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_APP_CLIENT_ID",
#     client_secret="YOUR_APP_CLIENT_SECRET",
#     redirect_uri="YOUR_APP_REDIRECT_URI",
#     scope="user-library-read"))

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])