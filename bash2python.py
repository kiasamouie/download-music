import requests
import os
import json
import re

# 1737177510, 1737177438, 1737177309, 1737177105, 1737176907, 1737176811, 1737176736, 1737176646, 1737176592, 1737176526, 1732090491

ids = [256134939,261913801,330146712,528760425,1177693117,252690175,256554681,529220967,252542071,279813935,252851780,101963800,895082899,256119050,825160387,1575934495,294097165,1813517757,253055613,803749093,149852040,256526897,255845880,1001890459]
with open(os.path.join('jsons', f'dnb.json'), 'r', encoding='utf8') as file:
    curl_command = """
        curl 'https://api-v2.soundcloud.com/playlists/1838743272?client_id=KhqBlYHkMDSGNC9DdLrcJHXqaLv5kOrh&app_version=1711450916&app_locale=en' \\
        -X 'PUT' \\
        -H 'Accept: application/json, text/javascript, */*; q=0.01' \\
        -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8,de;q=0.7,fa;q=0.6' \\
        -H 'Authorization: OAuth 2-294363-66593390-eXeioIxb0xltWzq' \\
        -H 'Connection: keep-alive' \\
        -H 'Content-Type: application/json' \\
        -H 'DNT: 1' \\
        -H 'Origin: https://soundcloud.com' \\
        -H 'Referer: https://soundcloud.com/' \\
        -H 'Sec-Fetch-Dest: empty' \\
        -H 'Sec-Fetch-Mode: cors' \\
        -H 'Sec-Fetch-Site: same-site' \\
        -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36' \\
        -H 'sec-ch-ua: "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"' \\
        -H 'sec-ch-ua-mobile: ?0' \\
        -H 'sec-ch-ua-platform: "Windows"' \\
        -H 'x-datadome-clientid: Mi9YF~jWZa0rGhro9aCL8TjxDTkESWoXyceDNyBnxB9HUzmT1ynN2BrFLrA9LsVW2w~WmAxWI6OybB63nEtA_d1AfMQ1kD_~JPng1~pLnUAqzhrLU3OLlW928FV05sei' \\
        --data-raw '{"playlist":{"tracks":[%s]}}' \\
        --compressed
    """ % ','.join(str(x) for x in ids)
    # """ % ','.join(str(x) for x in json.load(file)['dnb - 1'])

    method = re.search(r"-X '(\w+)'", curl_command).group(1)
    url = re.search(r"'([^']+)'", curl_command).group(1)
    headers = dict(re.findall(r"-H '([^:]+): (.*)'", curl_command))
    data = json.loads(re.search(r"--data-raw '({.*})'", curl_command).group(1))
    if method == 'PUT':
        response = requests.put(url, headers=headers, json=data)
        print(response)
