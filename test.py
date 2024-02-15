import requests

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,de;q=0.7,fa;q=0.6',
    'Authorization': 'OAuth 2-294363-66593390-eXeioIxb0xltWzq',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'https://soundcloud.com',
    'Referer': 'https://soundcloud.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'client_id': 'BE3UbKaeTvRBIgQh87b0PnePIWA4OH8g',
    'limit': '25',
    'offset': '0',
    'linked_partitioning': '1',
    'app_version': '1707232868',
    'app_locale': 'en',
}

response = requests.get('https://api-v2.soundcloud.com/me/play-history/tracks', params=params, headers=headers)