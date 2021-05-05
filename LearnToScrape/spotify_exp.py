import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import numpy as numpy
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

credentials = json.load(open('./LearnToScrape/JSON_Files/authorization.json'))
client_id = credentials['client_id']
client_secret = credentials['client_secret']

playlist_index = 0

# get the information in playlists_like_dislike
playlists = json.load(
    open('./LearnToScrape/JSON_Files/playlists_like_dislike.json'))
playlist_uri = playlists[playlist_index]['uri']
like = playlists[playlist_index]['like']

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# the URI is split by ':' to get the username and playlist ID
uri = playlist_uri
username = uri.split(':')[2]
playlist_id = uri.split(':')[4]


def get_playlist_tracks(username, playlist_id):
    results = sp.user_playlist_tracks(username, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks
    
results = sp.user_playlist(username, playlist_id, 'tracks')
print(results)
# Fetch the details of the track like ID's, Titles and Artists
playlist_tracks_data = results['tracks']
print(type(playlist_tracks_data))
print(type(get_playlist_tracks(username, playlist_id)))
playlist_tracks_id = []
playlist_tracks_titles = []
playlist_tracks_artists = []
playlist_tracks_first_artists = []

for track in playlist_tracks_data['items']:
    playlist_tracks_id.append(track['track']['id'])
    playlist_tracks_titles.append(track['track']['name'])
    # adds a list of all artists involved in the song to the list of artists for the playlist
    artist_list = []
    for artist in track['track']['artists']:
        artist_list.append(artist['name'])
    playlist_tracks_artists.append(artist_list)
    playlist_tracks_first_artists.append(artist_list[0])

# extracting audio features of each track
features = sp.audio_features(playlist_tracks_id)
features_df = pd.DataFrame(data=features, columns=features[0].keys())
# merging dataframes for getting audio features and track information
features_df['title'] = playlist_tracks_titles
features_df['first_artist'] = playlist_tracks_first_artists
features_df['all_artists'] = playlist_tracks_artists
# features_df = features_df.set_index('id')
features_df = features_df[['id', 'title', 'first_artist', 'all_artists',
                           'danceability', 'energy', 'key', 'loudness',
                           'mode', 'acousticness', 'instrumentalness',
                           'liveness', 'valence', 'tempo',
                           'duration_ms', 'time_signature']]
pd.set_option("display.max_rows", None)
print(features_df)

