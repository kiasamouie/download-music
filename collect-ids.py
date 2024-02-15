import yt_dlp
import os
import json
import sys
import random
import pyperclip
from datetime import timedelta

def split_list(ids):
    random.shuffle(ids)
    split = {}
    chunk_size = 30
    for i, n in enumerate(range(0, len(ids), chunk_size)):
        count = f' - {i+1}' if len(ids) > chunk_size else ""
        split[f'{title}{count}'] = ids[n:n+chunk_size]
    return split

def extract_info(url):
    return ydl.extract_info(url=url, download=False, process=False)

scan_all_tracks = False
track_seconds = timedelta(minutes=4).total_seconds()
playlists = json.loads(sys.argv[1])
os.makedirs('jsons', exist_ok=True)
for title in playlists:
    ids = []
    for artist in playlists[title]:
            with yt_dlp.YoutubeDL({}) as ydl:
                info = extract_info(f'https://soundcloud.com/{artist}')
                # pyperclip.copy(json.dumps(info))
                for entry in info['entries']:
                    id = entry['id']
                    if scan_all_tracks:
                        # no url
                        if entry['_type'] != "url":
                            continue
                        track = extract_info(entry["url"])
                        # track has a duration and is longer than 4 minutes
                        try:
                            if 'duration' in track and track['duration'] > track_seconds and 'view_count' in track and track['view_count'] != "None" and track['view_count'] > 9999:
                                continue
                        except:
                            print(track)
                            exit()
                    ids.append(int(id))
    ids = split_list(sorted(set(ids), key=lambda x: (x, ids.index(x))))
    filename = os.path.join('jsons',f'{title}.json')
    with open(filename, 'w', encoding="utf8") as file:
        json.dump(ids, file)
    for i in ids:
        print(i)
        print(len(ids[i]))
