from youtube_client import YoutubeClient

def run():
    youtube_client = YoutubeClient('./credits/client_id.json')
    playlists = youtube_client.get_playlists()


    for index, playlist in enumerate(playlists):
        print(f"{index}: {playlist.title}")
    choice = int(input("Enter your choice: "))
    chosen_playlist = playlists[choice] 
    print(f"You selected: {chosen_playlist.title} ")



if __name__ == '__main__':
    run()
