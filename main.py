from makeSimilarPlaylist import makeSimilarPlaylist
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import constants
import spotipy.util as util



# authenticate
authentication=SpotifyOAuth(scope=constants.SPOTIPY_SCOPE, client_id=constants.SPOTIPY_CLIENT_ID, 
    client_secret=constants.SPOTIPY_CLIENT_SECRET, redirect_uri=constants.SPOTIPY_REDIRECT_URI)
sp = spotipy.Spotify(auth_manager=authentication)

print('FINISHED')



