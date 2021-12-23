import constants
from deletePlaylists import deletePlaylists
from getAllLikedSongsURIs import getAllLikedSongsURIs

def makeLikedSongsPlaylist(sp):
    PLAYLIST_NAME = 'Liked_Songs_Playlist'
    # delete all playlists that have the same name
    deletePlaylists(PLAYLIST_NAME, sp)
    # get users 'liked songs' uris array
    uris = getAllLikedSongsURIs(sp)
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
    