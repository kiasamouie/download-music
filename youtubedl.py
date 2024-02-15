import youtube_dl
import os
import sys

# youtube
# url = 'https://www.youtube.com/watch?v=6ePDlq3Mtto'
# save = os.path.join('D:\\','Music','Single','')

# soundcloud
url = 'https://soundcloud.com/boudnb/bou-nokia-riddem'
# save = os.path.join('D:\\','Music',url.rsplit('/',1)[1].title(),'')
save = os.path.join('D:\\','Music','Single\\','')

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': save + '%(title)s.%(ext)s',
    'noplaylist': False,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }]
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

os.startfile(save)
