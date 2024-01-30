from pytube import YouTube
from pytube import Playlist


def main():
    print("----------")
    print("\nHello to YOUTUBE DOWNLOADER program using Python! (by Elisei P.)")
    while True:
        choice = input("\nDo you want to download:\n[v] just a video\n[p] an entire playlist\n\nYour answer ('v' or 'p'): ").lower()
        if choice == 'v':
            download_video()
            break
        elif choice == 'p':
            download_playlist()
            break
        else:
            print("ERROR: Not a valid choice. Try again.")
    print("\n----------")
    input("\nThank you for using my program!\nSee you next time!\nPress enter to close the program.\nBye! :) ")


def download_video():
    while True:
        link = input("\nEnter the video link: ")
        try:
            video = YouTube(link)
            video = video.streams.get_highest_resolution()
            video.download()
            break
        except:
            print("ERROR: Link not valid / wrong format / broken.")
    print("\nThe video has been downloaded successfully.")


def download_playlist():
    while True:
        link = input("\nEnter the playlist link: ")
        try:
            playlist = Playlist(link)
            playlist_len = len(playlist.video_urls)
            print(f'\nNumber of videos in playlist: {playlist_len}')
            for i, video_url in enumerate(playlist.video_urls):
                video = YouTube(video_url)
                video = video.streams.get_highest_resolution()
                video.download()
                print(f"Video download complete - {i+1}/{playlist_len} - {video.title}")
            break
        except:
            print("ERROR: Link not valid / wrong format / broken.")
    print("All videos has been downloaded successfully.")


if __name__ == "__main__":
    main()