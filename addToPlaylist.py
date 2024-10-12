import requests
import random


tracks = [ 1553840605, 1611607149, 1569334309, 1383559714, 1540834300, 1609089000, 1569105478, 1545617398, 1446996943, 1548168517, 1589435935, 1605339090, 1605048111, 1497245809, 1408187281, 1170479602, 1652653008, 1660703655, 748307200, 1684683774, 1687224123, 1735815861, 1742135715, 1737434064, 1764979737, 1773597627, 1506805582, 1687891359, 1755153255, 1632281796, 1793733829, 1808464929, 1806048750, 1808669349, 1833869895, 1462901266, 1029277984, 1839673416, 653255648, 1055182657, 1851831987, 1811941059, 1827065457, 1454010427 ]
random.shuffle(tracks)

headers = {
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
}

params = {
    'client_id': 'GnOdx9VmNzLeR9ljzVJQw5xAWmAOjNfb',
    'app_version': '1719931869',
    'app_locale': 'en',
}

json_data = {
    'playlist': {
        'tracks': tracks,
    },
}

response = requests.put('https://api-v2.soundcloud.com/playlists/1693368204', params=params, headers=headers, json=json_data)
print(response)