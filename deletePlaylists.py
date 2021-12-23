import constants
# params: a playlist name to be deleted, spotify
def deletePlaylists(playlist_name, sp):
    playlists = sp.user_playlists(constants.SPOTIFY_USERNAME)['items']
    for x in playlists:
        if x['name'] == playlist_name:
                sp.user_playlist_unfollow(constants.SPOTIFY_USERNAME, x['id'])