from deletePlaylists import deletePlaylists
from getAllLikedSongsURIs import getAllLikedSongsURIs
import numpy as np
import constants

def makeFeaturePlaylist(sp):
    # 'danceability','energy','key','loudness','mode', 'speechiness'
    # 'acousticness','instrumentalness','liveness','valence','tempo'
    # 'type','id','uri','track_href','analysis_url','duration_ms',
    # 'time_signature'


    FEATURE_NAME =  PLAYLIST_NAME = 'valence'
    # delete all playlists that have the same name
    deletePlaylists(PLAYLIST_NAME, sp)
    # get users 'liked songs' uris array
    uris = getAllLikedSongsURIs(sp)

    features = []
    offset = 0
        
    # max 100 tracks
    # get array of features for each song in liked songs
    while True:
        if ((offset + 100) > len(uris)):
            features.extend(sp.audio_features(uris[offset:]))
            break
        else:
            features.extend(sp.audio_features(uris[offset:(offset + 100)]))
            offset = offset + 100

    # swap until specific feature is ascending
    for i in range(0, len(features) - 1):
        smallest = [i, features[i][FEATURE_NAME]]
        for j in range(i, len(features)):
            if (features[j][FEATURE_NAME] < smallest[1] ):
                smallest =  [j, features[j][FEATURE_NAME]]
        features[i], features[smallest[0]] = features[smallest[0]], features[i]
    # get uris of ascended array
    uris = [i['uri'] for i in features]
    # get created playlist
    sp.user_playlist_create(constants.SPOTIFY_USERNAME, name=PLAYLIST_NAME)
    # get playlist id from newly cerated playlist
    PLAYLIST_ID = sp.user_playlists(constants.SPOTIFY_USERNAME)['items'][0]['id']
    
    # add tracks in 100s (max)
    while True:
        if len(uris) > 0:
            sp.user_playlist_add_tracks(constants.SPOTIFY_USERNAME, PLAYLIST_ID, uris[0:100])
            uris = uris[100:]
        else:
            break