# params: spotify
# returns uris array
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