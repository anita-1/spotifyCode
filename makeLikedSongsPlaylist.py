from getAllLikedSongsURIs import getAllLikedSongsURIs
from helperFunctions import deletePlaylists, makePlaylistAddTracks

def makeLikedSongsPlaylist(sp):
    PLAYLIST_NAME = 'Liked_Songs_Playlist'
    
    deletePlaylists(PLAYLIST_NAME, sp)
    
    uris = getAllLikedSongsURIs(sp)

    makePlaylistAddTracks(uris, PLAYLIST_NAME, sp)
    