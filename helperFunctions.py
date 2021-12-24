import constants

# params: a playlist name to be deleted, spotify
def deletePlaylists(playlist_name, sp):
    playlists = sp.user_playlists(constants.SPOTIFY_USERNAME)['items']
    for x in playlists:
        if x['name'] == playlist_name:
                sp.user_playlist_unfollow(constants.SPOTIFY_USERNAME, x['id'])

# params: spotify, uris array
# return: features array
def getFeaturesArray(sp, uris):
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
    return features

# params: spotify
# returns: uris array
def getAllLikedSongsURIs(sp):
    # uris array to store all uris
    uris=[]
    # increase offset every time to get all tracks
    offsetIndex = 0
    
    # continue this loop until <50 tracks are found
    while True:
        # get max 50 track ids
        results = sp.current_user_saved_tracks(limit=50, offset=offsetIndex)
        # add uris to array
        for items in results['items']:
            uris.append('spotify:track:' + items['track']['id'])

        # if end of 'liked songs' is reached, stop loop
        if len(results['items']) != 50:
            break
        
        # increment offsetIndex
        offsetIndex = offsetIndex + 50
    
    return uris

# params: array of uris of tracks, playlist name, spotify
def makePlaylistAddTracks(uris, PLAYLIST_NAME, sp):
    # make a playlist
    sp.user_playlist_create(constants.SPOTIFY_USERNAME, name=PLAYLIST_NAME)
    # get playlist id that was just created
    PLAYLIST_ID = sp.user_playlists(constants.SPOTIFY_USERNAME)['items'][0]['id']
    # add tracks in 100s (max)
    while True:
        if len(uris) > 0:
            sp.user_playlist_add_tracks(constants.SPOTIFY_USERNAME, PLAYLIST_ID, uris[0:100])
            uris = uris[100:]
        else:
            break