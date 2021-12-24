# I play with Spotify Web API here
using Spotipy and python 3

## Set Up
1. need to install spotipy package
2. need a constants.py with SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI, SPOTIPY_SCOPE, SPOTIFY_USERNAME (you'll need a spotify developer account + an app on it to get CLIENT_Xs)
3. SPOTIPY_REDIRECT_URI can be whatever you want, as long as its the same on the app on developer account
4. SPOTIFY_SCOPE should be 'user-library-read playlist-modify-public user-read-private user-read-playback-state user-modify-playback-state'

## Run
run all functions using main.py, after the authentications
