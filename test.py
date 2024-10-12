import requests

def getSpecialSubstring(s, k, charValue):
    # Map each character to its special value based on charValue
    special_values = {chr(i + ord('a')): int(charValue[i]) for i in range(26)}

    max_length = 0
    left = 0
    zero_count = 0

    # Sliding window approach
    for right in range(len(s)):
        # Check if the current character is a `0`-mapped character
        if special_values[s[right]] == 0:
            zero_count += 1

        # If zero_count exceeds `k`, move the left pointer to the right
        while zero_count > k:
            if special_values[s[left]] == 0:
                zero_count -= 1
            left += 1
        
        # Update maximum length of valid substring
        max_length = max(max_length, right - left + 1)

    return max_length

def getArticleTitles():
    url = 'https://jsonmock.hackerrank.com/api/articles'
    titles = []
    page = 1
    
    # Fetch the first page to get total pages
    response = requests.get(url, params={'author': 'epaga', 'page': page})
    if response.status_code == 200:
        data = response.json()
        total_pages = data['total_pages']
        
        # Iterate through all pages
        while page <= total_pages:
            response = requests.get(url, params={'author': 'epaga', 'page': page})
            if response.status_code == 200:
                data = response.json()
                for article in data['data']:
                    # Append title or story_title if available
                    title = article.get('title')
                    story_title = article.get('story_title')
                    if title:
                        titles.append(title)
                    elif story_title:
                        titles.append(story_title)
            
            page += 1
    print(titles)
    return '\n'.join(titles)

if __name__ == '__main__':
    result = getSpecialSubstring('giraffe', 2, '01111001111111111011111111')
    print(result)
    # print(getArticleTitles())
