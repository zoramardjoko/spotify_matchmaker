from __future__ import print_function  # (at top of module)
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import math

clientId = 'c8a46e5dad444f8d9e108ed1065b5fc3'
clientSecret = '01e8603f1e684bddbcbb12ac81264a52'
redirectUrl = 'http://localhost:8888/callback'
scope = "user-library-read user-follow-read user-top-read"

authManager = SpotifyOAuth(client_id=clientId, client_secret=clientSecret, redirect_uri=redirectUrl, scope=scope)

sp = spotipy.Spotify(auth_manager=authManager)

user = sp.current_user()
ranges = ['long_term']  # we are looking at long-term top songs from user
names = []  # stores the names of the top tracks
u = []  # uris of the tracks
size = int(input('How many of your top songs would you like to consider? Must be between 2 and 50 '))
for sp_range in ranges: # get names of top tracks
    results = sp.current_user_top_tracks(time_range=sp_range, limit=size)
    for i, item in enumerate(results['items']):
        names.append(item['name'])  # add name
        print(i, item['name'], '//', item['artists'][0]['name'])  # print for convenience
    print()

for i, item in enumerate(results['items']):  # add their uris to a list
    u.append(item['uri'])

dance_ability = []  # these 3 lists will keep track of their respective scores for each track
energy = []
acousticness = []
features = sp.audio_features(u)  # run audio features on uris of top tracks
for feature in features:  # keep track of danceability, energy, and acousticness
    dance_ability.append(feature['danceability'])
    energy.append(feature['energy'])
    acousticness.append(feature['acousticness'])

magnitude = []
for i in range(size):  # calculates the magnitude for each song based on danceability, energy, and acousticness
    squared = pow(dance_ability[i], 2) + pow(energy[i], 2) + pow(acousticness[i], 2)
    magnitude.append(math.sqrt(squared))

matrix = []
for i in range(size):
    row = [0] * size  # create a row with 4 zeros
    matrix.append(row)

for i in range(size):  # for each pair of songs, we calculate dot products
    for j in range(size):
        d = dance_ability[i] * dance_ability[j]
        e = energy[i] * energy[j]
        a = acousticness[i] * acousticness[j]
        matrix[i][j] = d + e + a

ans = []
for i in range(size):
    row = [0] * size  # create a row with 4 zeros
    ans.append(row)

for i in range(size):  # calculate similarity based on magnitude and dot products for each pair of songs
    for j in range(size):
        mag = magnitude[i] * magnitude[j]
        ans[i][j] = matrix[i][j]/mag

maxSim = 0
ind1 = 0
ind2 = 0
for i in range(size):  # find max similarity value
    for j in range(size):
        if maxSim < ans[i][j] and i != j:
            maxSim = ans[i][j]
            ind1 = i
            ind2 = j
print(names[ind1] + " and " + names[ind2] + "are the most similar songs based on danceability, energy, "
                                            "and acousticness")

print("The danceability of " + names[ind1] + " and " + names[ind2] + " are: " + str(dance_ability[ind1]) + " and " + str(dance_ability[ind2]) + ", respectively")
print("The energy of " + names[ind1] + " and " + names[ind2] + " are: " + str(energy[ind1]) + " and " + str(energy[ind2]) + ", respectively")
print("The acousticness of " + names[ind1] + " and " + names[ind2] + " are: " + str(acousticness[ind1]) + " and " + str(acousticness[ind2]) + ", respectively")
