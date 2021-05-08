# simple program to try to scrape multiple playlists
# relies on both playlists_like_dislike.json as well as authorization.json to try to loop through everything

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import numpy as numpy
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# implementing mysql connector
import mysql.connector

# establish the credentials to authorize the user to 
credentials = json.load(open('./LearnToScrape/JSON_Files/authorization.json'))
client_id = credentials['client_id']
client_secret = credentials['client_secret']

# get the information in playlists_like_dislike
playlists = json.load(
    open('./LearnToScrape/JSON_Files/playlists_like_dislike.json'))


# using the minor_key and major_key hash maps in order to make it easier
# for us to associate each of the songss
minor_key = {
    0: "c  min",
    1: "c# min",
    2: "d  min",
    3: "d# min",
    4: "e  min",
    5: "f  min",
    6: "f# min",
    7: "g  min",
    8: "g# min",
    9: "a  min",
    10: "a# min",
    11: "b  min"
}

major_key = {
    0: "C  Maj",
    1: "C# Maj",
    2: "D  Maj",
    3: "D# Maj",
    4: "E  Maj",
    5: "F  Maj",
    6: "F# Maj",
    7: "G  Maj",
    8: "G# Maj",
    9: "A  Maj",
    10: "A# Maj",
    11: "B  Maj"
}

# connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Spelling4bees!?!!",
    database="Spotify_Play_Data"
)

val = []
mycursor = mydb.cursor()

"""
for playlist_index in range(0, len(playlists)):
    playlist_uri = playlists[playlist_index]['uri']
    like = playlists[playlist_index]['like']

    client_credentials_manager = SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # the URI is split by ':' to get the username and playlist ID
    uri = playlist_uri
    username = uri.split(':')[2]
    playlist_id = uri.split(':')[4]

    # you must scroll through them to view more than just the max limit
    def get_playlist_tracks(username, playlist_id):
        results = sp.user_playlist_tracks(username, playlist_id)
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
        return tracks

    playlist_tracks_id = []
    playlist_tracks_titles = []
    playlist_tracks_artists = []
    playlist_tracks_first_artists = []

    id_list = []
    tempo_list = []
    key_list = []
    mode_list = []
    act_key_list = []

    results = get_playlist_tracks(username, playlist_id)

    # each one is a dictionary so we must iterate through them all!
    for track in range(0, len(results)):
        # get rid of the ones that are under copyright revision
        if results[track]['track']['id'] is None:
            continue
        else:
            playlist_tracks_id.append(results[track]['track']['id'])
            playlist_tracks_titles.append(results[track]['track']['name'])
            artist_list = []
            # there may be multiple artists, try to iterate through those instead
            for artist in results[track]['track']['artists']:
                artist_list.append(artist['name'])
            playlist_tracks_artists.append(artist_list)
            playlist_tracks_first_artists.append(artist_list[0])

    # access each of the elements in the song
    for each_id in playlist_tracks_id:
        feature = sp.audio_features(each_id)
        if feature[0] is None:
            continue
        else:
            id_list.append(feature[0]['id'])
            tempo_list.append(feature[0]['tempo'])
            key_list.append(feature[0]['key'])
            mode_list.append(feature[0]['mode'])

    for each_mode in mode_list:
        # if it's major
        if each_mode == 1:
            act_key_list.append(major_key[key_list[each_mode]])
        else:
            act_key_list.append(minor_key[key_list[each_mode]])
    
    # there are len(results) to insert each time
    for x in range(0, len(results)):
        val.append((playlist_tracks_titles[x], playlist_tracks_first_artists[x],
                         id_list[x], str(tempo_list[x]), act_key_list[x]))


for x in range(0, len(val)):
    mycursor = mydb.cursor()
    sql = "INSERT INTO song_playlist (title, first_artists, id, tempo, music_key) VALUES (%s, %s, %s, %s, %s)"
    mycursor.execute(sql, val[x])
    mydb.commit()
"""

mycursor.execute("SELECT * FROM song_playlist")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

        
    



