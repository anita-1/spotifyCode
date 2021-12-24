from helperFunctions import deletePlaylists, getAllLikedSongsURIs, getFeaturesArray, makePlaylistAddTracks

def makeSimilarPlaylist(sp):    
    PLAYLIST_NAME = 'Samesies'

    uris = getAllLikedSongsURIs(sp)

    features = getFeaturesArray(sp, uris)

    # large value of mainSum to compare to 
    mainSum = 10000

    # find the first 2 most similar by comparing each track with the other ones
    for i in range(0, len(features) - 1):
        for j in range(i + 1, len(features)):
            differences = {x: features[j][x] - features[i][x] for x in ['instrumentalness', 'acousticness', 'liveness', 'speechiness',
                'energy', 'danceability', 'valence']}
            # the smaller the sum of the differences, the more similar they are
            sum = 0
            for x in differences:
                differences[x] = round(abs(differences[x]), 4)
                sum = sum + differences[x]
            sum = round(sum, 4)
            if(sum < mainSum):
                mainSum = sum 
                indices = [i, j]
            
    # make a sort array and add the 2 track objects to it, deleting from features
    sort=[]
    for x in range(0, len(indices)):
        sort.append(features[indices[x] - x])
        del (features[indices[x] - x])

    # compare last sorted element with each in features 
    # add song that is most similar to the last song
    while(len(features) > 1):
        lastElementSort = sort[len(sort) - 1]
        mainSum = 10000
        for i in range(0, len(features)):
            differences = {x: lastElementSort[x] - features[i][x] for x in ['instrumentalness', 'acousticness', 'liveness', 'speechiness',
            'energy', 'danceability', 'valence']}
            sum = 0
            for x in differences:
                differences[x] = round(abs(differences[x]), 4)
                sum = sum + differences[x]
            sum = round(sum, 4)
            if(sum < mainSum):
                mainSum = sum 
                indices = [i]
        sort.append(features[indices[0]])
        del features[indices[0]]
        
    sort.append(features[0])
    del features[0]
    
    # change from features array of lists to uris array
    uris = [i['uri'] for i in sort]

    deletePlaylists(PLAYLIST_NAME, sp)

    makePlaylistAddTracks(uris, PLAYLIST_NAME, sp)
