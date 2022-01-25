# I play with Spotify Web API here (mainly making playlists)
using Spotipy and Python3 with VS Code

## Set Up
1. A SPOTIFY DEVELOPER ACCOUNT, go to spotify website and apply using your existing account or create a new account
<br/> Create an app on that account to get CLIENT_Xs that we'll use later
2. Install Spotipy package for Python
3. Create a ```constants.py``` in this same directory with SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI, SPOTIPY_SCOPE, SPOTIFY_USERNAME variables <br/> 
a. SPOTIPY_REDIRECT_URI can be whatever you want, as long as its the same on the app on developer account <br/>
b. SPOTIFY_SCOPE should be 'user-library-read playlist-modify-public user-read-private user-read-playback-state user-modify-playback-state' <br/>
c. Fill the rest in according to your app

## Run
run all functions by importing(? I forgot if needed) function from file before authentication and writing the function with respective parameters in ```main.py``` after the authentications

### How to Create a Playlist from your "Liked Songs" Section on Spotify:
1. Copy ```main.py```, ```makeLikedSongsPlaylist.py```, ```helperFunctions.py``` into a directory.
2. Do above "Set Up"
3. (?) Write ```import makeLikedSongsPlaylist from makeLikedSongsPlaylist``` on line 7, before the authentication
4. Write ```makeLikedSongsPlaylist(sp)``` on line 13, after the authentication.
5. Run main program.

## NOTE:
all functions require songs in your Liked Songs on this developer account you are using

## Files
```main.py``` authenticates, runs your wanted function, prints FINISHED when done <br/> 

```makeLikedSongsPlaylist.py``` requires one parameter: Spotipy authenication object, deletes playlists with the same name, gets all the tracks from your Liked Songs and creates a playlist for you called 'Liked_Songs_Playlist' that can be changed. <br/>

```makeFeaturePlaylist.py``` requires one parameter: Spotipy authenication object, deletes playlists with the same name, gets all the tracks from your Liked Songs, creates an ascending playlist for you based on a song feature you choose in FEATURE_NAME, and names it 'FEATURE_NAME' that can be changed. <br/>

```makeSimilarPlaylist.py``` requires one parameter: Spotipy authenication object, deletes playlists with the same name, gets all the tracks from your Liked Songs, creates a playlist with the most similar song remaining following the last added song, and names it 'Samesies' that can be changed. <br/>

```helperFunctions.py``` contains a bunch of helper functions to help above listed functions such as ```deletePlaylists(playlist_name, sp)```, ```getFeaturesArray(sp, uris)```, ```getAllLikedSongsURIs(sp)```, ```makePlaylistAddTracks(uris, PLAYLIST_NAME, sp)``` all which are self-explanatory I think.

See code for specific comments

## What I Learned
1. Everything is pretty repetitive. 
2. Spotipy is really helpful. Make sure you're on their documentation and not Spotify's. 

## Potholes
1. You MUST have a Spotify developer account with an **app** to get those keys. 
2. You MUST have songs in your "Liked Songs" section in said Spotify developer account. 

## What's Next
1. I am pretty sure ```makeSimilarPlaylist.py``` is not sorting correctly but I do not have time to fix it right now. <br/>
2. I would like to have the code be more flexible such as using a playlist to create another but that is a later problem. <br/>
3. Other stuff using Spotipy maybe.
