import json 
import spotipy 
import webbrowser

#username = 'trinityung'
clientID = '4dbcdca3b82d44359c9171d1bdddd60e'
clientSecret = '3ced917a6dc64047b7a5d4634d28512a'
redirect_uri = 'http://localhost:3000/'

oauth_object = spotipy.SpotifyOAuth(
    clientID,
    clientSecret,
    redirect_uri,
    scope='user-library-read user-read-playback-state user-modify-playback-state'
)

token_dict = oauth_object.get_access_token() 
token = token_dict['access_token'] 
spotifyObject = spotipy.Spotify(auth=token) 
user_name = spotifyObject.current_user() 

# To print the JSON response from  
# browser in a readable format. 
# optional can be removed 
print(json.dumps(user_name, sort_keys=True, indent=4)) 

mood_to_song = {
    'happy': 'https://open.spotify.com/track/3bBVGKs0efN45YGAVoBfCy?si=243f99d7bd6f42fc',
    'sad': 'https://open.spotify.com/track/3KW83sMHyAxbRHapJA3bMY?si=27d8a859166544cb',
    'mad': 'https://open.spotify.com/track/3NODaFePbYJpp5VAY1ipYp?si=f88882d205bc4f66',
}

while True: 
    selected_mood = input("Enter a mood: ") #get the emotions based on facial recognition
    if selected_mood in mood_to_song:
        song_uri = mood_to_song[selected_mood]
        # Start playback
        spotifyObject.start_playback(uris=[song_uri])
    else:
        break


    '''
    print("Welcome to the project, " + user_name['display_name']) 
    print("0 - Exit the console") 
    print("1 - Search for a Song") 
    user_input = int(input("Enter Your Choice: ")) 
    if user_input == 1: 
        search_song = input("Enter the song name: ") 
        results = spotifyObject.search(search_song, 1, 0, "track") 
        songs_dict = results['tracks'] 
        song_items = songs_dict['items'] 
        song = song_items[0]['external_urls']['spotify'] 
        webbrowser.open(song) 
        print('Song has opened in your browser.') 
    elif user_input == 0: 
        print("Good Bye, Have a great day!") 
        break
    else: 
        print("Please enter valid user-input.") 
'''
