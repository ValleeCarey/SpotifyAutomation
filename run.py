from youtube_client import YoutubeClient

def run():
    #get a list of playlist from youtube 
    youtube_client = YoutubeClient('./credits/client_id.json')
    playlists = youtube_client.get_playlists()

# ask which playlist we want to get the music video from  
    for index, playlist in enumerate(playlists):
        print(f"{index}: {playlist.title}")
    choice = int(input("Enter your choice: "))
    chosen_playlist = playlists[choice] 
    print(f"You selected: {chosen_playlist.title} ")

#for each video in the playlist get song info from Youtube

songs = youtube_client.get_videos_from_playlist(chosen_playlist.id)
print(f"Attempting to add {len(songs)}")

#search for spotify song 



if __name__ == '__main__':
    run()
