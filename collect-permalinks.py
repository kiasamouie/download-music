import youtube_dl
import os
import json
import sys
import random

artists = []
with youtube_dl.YoutubeDL({}) as ydl:
    try:
        playlist_url = f'https://soundcloud.com/inexed/sets/q-u-e-s-t-synthwave-chillwave'
        info = ydl.extract_info(url=playlist_url, download=False, process=False)
        for url in [entries['url'] for entries in info['entries']]:
            artists.append(ydl.extract_info(url, download=False, process=False)['uploader_url'].split("/")[-1])
        with open(f"{os.path.join('jsons', playlist_url.split('/')[-3])}.json", 'w', encoding="utf8") as file:
            json.dump(artists, file, indent=4)
    except:
        exit()
