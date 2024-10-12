import os
import subprocess
url = 'https://www.youtube.com/watch?v=r2G1WPpgg8g'
save = os.path.join('D:\\', 'Music', 'Single\\')
download_cmd = [
    'yt-dlp',
    '--format', 'bestaudio/best',
    '--extract-audio',
    '--audio-format', 'wav',
    '--audio-quality', '320K',
    '--output', os.path.join(save, '%(title)s.%(ext)s'),
    url
]
subprocess.run(download_cmd)
os.startfile(save)
