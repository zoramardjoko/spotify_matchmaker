Name: Spotipy Matchmaker

Description: This project allows the user to interact with their own spotify
profiles and choose from 3 different options for information. From the GUI,
the user can click on the button, “Get a new playlist,” and our code will
create a new playlist for you, using your top artists to make recommendations
of top songs from related artists. The user can also click on the button,
“Find out your two most similar songs,” and our code will return the two
songs in your current top tracks that are the most similar. The user can also
click on the button, “Get related artists,” and our code will output artists that
are between one degree and three degrees to the artist you input.

Artist Collaborator Network: This functionality allows the user to input an
artist and find a network of collaborators. Starting with the input artist, the
program will find that artist’s top 10 songs and find any collaborators from
those songs. Then, for each collaborator, the program will find their top ten
songs, those songs’ collaborators, and so on. The program will continue until
the network is 3 steps away from the original artist. The program will then
return a list of artists that are 1 step away from the original artist, 2 steps
away, and 3 steps away. If the original artist does not have any collaborators
in their top songs, the program will prompt for another artist. The program
takes a bit to run as the network gets larger and larger as it continues outward
from the source. The print statements happening throughout the program
are the urls of each artist’s top songs and the collaborators of those songs
if there are any.

Create a Playlist of Recommendations:This function will look at the user’s
recent top artists, and generate a related artist for each top artist. This
generation of related artists uses data from the Spotify listening community.
Next, it will add an empty playlist to the user’s library. The program will find
each related artist’s top five songs and add them to the playlist.

Find out your two most similar songs: This function goes through the user’s
top x songs (x is a number input by the user and must be between 2 and 50)
and uses cosine similarity to compare the songs based on danceability,
energy, and acousticness. Each track has a value associated with them for
each of these factors.

Process: We used Spotipy to get data from a user, such as their top artists.
“Spotipy is a lightweight Python library for the Spotify Web API. With Spotipy
you get full access to all of the music data provided by the Spotify platform.”
Spotipy streamlined the user authentication process, which we originally had
a lot of trouble with because we used a different method. Additionally,
Spotipy contains many built in methods that we were able to use in our
program. Also, we created our own Spotify app for this project.

Rate-Limiting Issues: Because our program makes so many requests, we were
rate limited pretty quickly. We noticed that the programs weren’t running
properly, an issue that stopped when we switched users or created a new
app. If any issues are encountered when running this code, please reach out
to us, and we will create a new app to run.

Categories: For our project, we implemented Graphs and Graph Algorithms,
recommendations, and Document Search. For Graph algorithms, we created a
graph based on a “source” artist that the user inputs. We also made song
recommendations using the property of triadic closure. If you like an artist,
and that artist is related to another artist (based on analysis of the Spotify
community's listening history), then you are likely to enjoy the related artist’s
top tracks. Lastly, we used the idea of cosine similarity to analyze similarity of
songs, based on their danceability, energy, and acousticness attributes.

Changes: We initially had different ideas like creating a graph for followers
and finding compatibility between users. However, we were not able to
implement parts of these because there is no way to access a follower’s
followers. Some parts of our original ideas were also too simple, and we
received feedback from our TA on what project ideas could be better
implemented, and how we could add complexity to other ideas.

Work Breakdown: Initially, we had a work breakdown that was very horizontal, meaning that one group member would have to wait for the others to finish before they could start working. In order to create a more vertical work breakdown, we decided to each focus on working on one feature, and then collaborate at the end to combine our work into one app. Shruthi did song similarity and created the GUI, Zora did create a playlist based on recommendations, and Brandon did the artist collaborator network.

We met often to discuss our goals, how we wanted to combine everything, and importantly, helped each other debug. This is our first project working with an API like Spotify, and we all have never coded in Python before.
