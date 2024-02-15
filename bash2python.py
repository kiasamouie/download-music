import requests
import os
import json
import re

# 1737177510, 1737177438, 1737177309, 1737177105, 1737176907, 1737176811, 1737176736, 1737176646, 1737176592, 1737176526, 1732090491

with open(os.path.join('jsons', f'synthwave.json'), 'r', encoding='utf8') as file:
    curl_command = """
        curl 'https://api-v2.soundcloud.com/playlists/1732090491?client_id=BE3UbKaeTvRBIgQh87b0PnePIWA4OH8g&app_version=1707232868&app_locale=en' \\
        -X 'PUT' \\
        -H 'Accept: application/json, text/javascript, */*; q=0.01' \\
        -H 'Accept-Language: en-US,en;q=0.9' \\
        -H 'Authorization: OAuth 2-294516-1332501624-OByaKdzbFOxRu' \\
        -H 'Connection: keep-alive' \\
        -H 'Content-Type: application/json' \\
        -H 'Origin: https://soundcloud.com' \\
        -H 'Referer: https://soundcloud.com/' \\
        -H 'Sec-Fetch-Dest: empty' \\
        -H 'Sec-Fetch-Mode: cors' \\
        -H 'Sec-Fetch-Site: same-site' \\
        -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36' \\
        -H 'sec-ch-ua: "Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"' \\
        -H 'sec-ch-ua-mobile: ?0' \\
        -H 'sec-ch-ua-platform: "Windows"' \\
        --data-raw '{"playlist":{"tracks":[%s]}}' \\
        --compressed
    """ % ','.join(str(x) for x in json.load(file)['synthwave - 11'])

    method = re.search(r"-X '(\w+)'", curl_command).group(1)
    url = re.search(r"'([^']+)'", curl_command).group(1)
    headers = dict(re.findall(r"-H '([^:]+): (.*)'", curl_command))
    data = json.loads(re.search(r"--data-raw '({.*})'", curl_command).group(1))
    if method == 'PUT':
        response = requests.put(url, headers=headers, json=data)
        print(response)
