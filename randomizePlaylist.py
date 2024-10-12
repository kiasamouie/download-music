import youtube_dl
import requests
import random

tracks = []
with youtube_dl.YoutubeDL({}) as ydl:
    try:
        playlist_url = f'https://soundcloud.com/thekiadoe/sets/dnb'
        info = ydl.extract_info(url=playlist_url, download=False, process=False)
        for entries in info['entries']:
            tracks.append(int(ydl.extract_info(entries['url'], download=False, process=False)['id'].split("/")[-1]))
        random.shuffle(tracks)

        response = requests.put(
            f"https://api-v2.soundcloud.com/playlists/{info['id']}", 
            params={
                'client_id': 'GnOdx9VmNzLeR9ljzVJQw5xAWmAOjNfb',
                'app_version': '1719931869',
                'app_locale': 'en',
            }, 
            headers={
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,de;q=0.7,fa;q=0.6',
                'Authorization': 'OAuth 2-294363-66593390-eXeioIxb0xltWzq',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'DNT': '1',
                'Origin': 'https://soundcloud.com',
                'Referer': 'https://soundcloud.com/',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'x-datadome-clientid': 'jb5YHWJw74_tLGc3eqlUYvS~i1XhIL0iewZJSCjgU~_k7m4TjfqSItodzfZV_8jcMW1kLLZVDzNN7LOrW8zoBzhcDjJ9GGwtcjuFaNKcKHm_dtw9wiED4FDfe0aCHcTF',
            }, 
            json={
                'playlist': {
                    'tracks': tracks,
                },
            }
        )
        print(response)
    except:
        exit()
