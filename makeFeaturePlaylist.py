from helperFunctions import deletePlaylists, getAllLikedSongsURIs, getFeaturesArray, makePlaylistAddTracks

def makeFeaturePlaylist(sp):
    # 'danceability','energy','key','loudness','mode', 'speechiness'
    # 'acousticness','instrumentalness','liveness','valence','tempo'
    # 'type','id','uri','track_href','analysis_url','duration_ms',
    # 'time_signature's

    FEATURE_NAME =  PLAYLIST_NAME = 'valence'
    
    deletePlaylists(PLAYLIST_NAME, sp)
    
    uris = getAllLikedSongsURIs(sp)

    features = getFeaturesArray(sp, uris)

    # swap until specific feature is ascendings
    for i in range(0, len(features) - 1):
        smallest = [i, features[i][FEATURE_NAME]]
        for j in range(i, len(features)):
            if (features[j][FEATURE_NAME] < smallest[1] ):
                smallest =  [j, features[j][FEATURE_NAME]]
        features[i], features[smallest[0]] = features[smallest[0]], features[i]
    # get uris of ascended array from features
    uris = [i['uri'] for i in features]

    makePlaylistAddTracks(uris, PLAYLIST_NAME, sp)