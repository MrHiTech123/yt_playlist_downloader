from sys import argv
from os import system


print(argv)

try:
    playlist_url = argv[1]
    playlist_length = int(argv[2])
except Exception:
    print('Usage: dlp_list playlist_url playlist_length')
    raise SystemExit(0)


for i in range(playlist_length):
    # According to the internet, this should result in every video in the playlist from index 1 to (i + 1) being downloaded.
    # In my experience, it only downloads the video at index (i + 1), hence the for loop.
    system(f'yt-dlp --playlist-items {i + 1} {playlist_url}')
