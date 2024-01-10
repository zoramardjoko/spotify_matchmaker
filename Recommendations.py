import spotipy
from spotipy.oauth2 import SpotifyOAuth

clientId = 'e1b5c81aab2b4d37abc436d9685f3d07'
clientSecret = 'cf66db0cb274474b9d31385d6cfeb597'
redirectUrl = 'http://localhost:8888/callback'
scope = "user-library-read playlist-read-private user-top-read playlist-modify-public"

authManager = SpotifyOAuth(client_id=clientId, client_secret=clientSecret, redirect_uri=redirectUrl, scope=scope)

sp = spotipy.Spotify(auth_manager=authManager)

user = sp.current_user()

top_artists = sp.current_user_top_artists(limit=20,time_range='short_term')
# can change parameter to short_term or medium_term if preferred

i = 0;
list_of_artists = [] # artist ids
names_of_artists = [] # artist names
for x in top_artists["items"]:
    if (i < 20):
        list_of_artists.append(x['id'])
        names_of_artists.append(x['name'])

    i = i + 1
# list_of_artists now contains user's all time top 20 artists

# uses spotipy's built in function to get related artists
# Similarity is based on analysis of the Spotify community's listening history.
related_artists = []
for artist in list_of_artists:
    related_artists.append(sp.artist_related_artists(artist))

ids = []
for artist in related_artists:
    if artist ['artists'] != []:
        ids.append(artist['artists'][0]['id'])

songs_to_add = []
for artist_id in ids:
    songs = sp.artist_top_tracks(artist_id=artist_id)
    i = 0
    for track in songs['tracks']:
        if (i < 5):
            songs_to_add.append(track['id'])
            i = i + 1
# at this point, songs_to_add is populated with top 5 songs of all related artists

# make a playlist for the user
playlist = sp.user_playlist_create(user= user['id'], name='Recommended Songs for You!', description="Made by "
                                                                                                    "Brandon, Shruthi, "
                                                                                                    "Zora")
playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=songs_to_add)