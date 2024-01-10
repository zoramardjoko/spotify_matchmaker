import urllib

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# initializes spotify api through client ID and client secret. The functionality of
# this program does not require authorization
clientId = 'e1b5c81aab2b4d37abc436d9685f3d07'
clientSecret = 'cf66db0cb274474b9d31385d6cfeb597'

clientCredentialsManager = SpotifyClientCredentials(client_id=clientId, client_secret=clientSecret)

spotipyApi = spotipy.Spotify(client_credentials_manager=clientCredentialsManager)

# Creates 4 lists, one to keep track of already visited artists so that the program
# does not loop back on itself, and then lists to store the collaborators at each level
alreadyVisited = []
alreadyVisited0 = []
alreadyVisited1 = []
alreadyVisited2 = []
alreadyVisited3 = []

# method to recursively look through artists and their collaborators
def artistNetwork(id, step):
    # adds current artist to list of already discovered artists
    alreadyVisited.append(id)

    # adds artist to specific list depending on how far they are from the original artist
    if (step == 0):
        alreadyVisited0.append(id)
        print(alreadyVisited0)
        print(step)
    if (step == 1):
        alreadyVisited1.append(id)
        print(alreadyVisited1)
        print(step)
    if (step == 2):
        alreadyVisited2.append(id)
        print(alreadyVisited2)
        print(step)
    if (step == 3):
        alreadyVisited3.append(id)
        print(alreadyVisited3)
        print(step)

    print('spotify:artist:' + id)

    # finds top 10 tracks of this artist
    response = spotipyApi.artist_top_tracks('spotify:artist:' + id)

    collabs = 0;

    # moves through the information provided by the .artist_top_tracks() method
    # to find the collaborators of the songs
    for track in response['tracks']:
        print(track['id'])
        id = track['id']
        print(track['name'])
        print(track['external_urls']['spotify'])
        trackInfo = spotipyApi.track(id)
        artistInfo = trackInfo['artists']
        # artistInfo will be of size 1 if there are no collaborators
        if (len(artistInfo) > 1):
            collabs = collabs + 1
            # looks through each collaborator and gets their ID
            for i in range(len(artistInfo)):
                artist = artistInfo[i]
                print(artist['name'] + ': ' + artist['id'])
                newId = artist['id']
                # makes sure that the program will only go 3 steps from the original artist
                if (step + 1 <= 3):
                    # the try-catch statement allows for the program to see if an artist
                    # has already been visited
                    try:
                        alreadyVisited.index(newId)
                    except ValueError as e:
                        artistNetwork(newId, step + 1)

    # statement that runs if the original artist does not have any collaborators
    if (collabs == 0):
        if (step == 0):
            print(
                'Sorry! This artist does not have collaborators in their top songs. Please try and entering another artist.')
            takeInput()

# method to initially take the input of the user for the original artist
def takeInput():
    name = input("Choose an artist: ")

    # uses search functionality to grab artist ID from the input name
    try:
        artist = spotipyApi.search(name)
    except urllib.error.URLError as e:
        print("Invalid artist", e)

    info = artist['tracks']['items'][0]

    for i, artist in enumerate(info['artists']):
        id = artist['id']
        break

    # runs first call of graph method on the original artist
    artistNetwork(id, 0)


takeInput()

# after artistNetwork() method is run, program prints out the artists 1, 2, and 3
# steps away from the original artist
print('Artists 0 steps from original: ')
for i in range(len(alreadyVisited0)):
    artistId = 'spotify:artist:' + alreadyVisited0[i]
    artist = spotipyApi.artist(artistId)
    print(artist['name'])

print('--------------------------------')

print('Artists 1 step from original: ')
for i in range(len(alreadyVisited1)):
    artistId = 'spotify:artist:' + alreadyVisited1[i]
    artist = spotipyApi.artist(artistId)
    print(artist['name'])

print('--------------------------------')

print('Artists 2 steps from original: ')
for i in range(len(alreadyVisited2)):
    artistId = 'spotify:artist:' + alreadyVisited2[i]
    artist = spotipyApi.artist(artistId)
    print(artist['name'])

print('--------------------------------')

print('Artists 3 steps from original: ')
for i in range(len(alreadyVisited3)):
    artistId = 'spotify:artist:' + alreadyVisited3[i]
    artist = spotipyApi.artist(artistId)
    print(artist['name'])
