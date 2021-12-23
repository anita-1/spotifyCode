import spotipy
from spotipy.oauth2 import SpotifyOAuth
import constants
import spotipy.util as util
import json
import os
from os import path
import time
import random

# authenticate
authentication=SpotifyOAuth(scope=constants.SPOTIPY_SCOPE, client_id=constants.SPOTIPY_CLIENT_ID, 
    client_secret=constants.SPOTIPY_CLIENT_SECRET, redirect_uri=constants.SPOTIPY_REDIRECT_URI)
sp = spotipy.Spotify(auth_manager=authentication)

# get users 'liked songs'
results = sp.current_user_saved_tracks(limit=50, offset=0)
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])



