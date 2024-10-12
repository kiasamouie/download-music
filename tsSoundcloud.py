import subprocess
import os
import json

# https://soundcloud.com/simula/simula-iii-1

def get_track_info(url):
    return json.loads(subprocess.run(
        ["yt-dlp", url, "-J"],
        capture_output=True,
        text=True
    ).stdout)
def sanitize_title(title):
    return "".join([c if c.isalnum() else "_" for c in title])
def create_snippet(input_file, ss, to, output_file):
    snippet_command = ["ffmpeg", "-i", input_file, "-ss", ss, "-to", to, "-c:a", "pcm_s16le", "-ar", "44100", f"{output_file}.wav"]
    subprocess.call(snippet_command)
soundcloud_url = "https://soundcloud.com/simula/simula-iii-1"
timestamps = [
    ("00:01:05","00:02:11"),
    ("00:02:44","00:03:37"),
    ("00:04:20","00:05:23"),
    ("00:05:25","00:06:09"),
    ("00:06:09","00:07:13"),
    ("00:07:14","00:07:55"),
    ("00:11:10","00:12:14"),
    ("00:12:15","00:12:45"),
    ("00:13:42","00:15:07"),
    ("00:15:07","00:15:50"),
    ("00:15:50","00:16:32"),
    ("00:16:34","00:17:08"),
    ("00:18:20","00:19:04"),
    ("00:19:06","00:19:46"),
    ("00:21:04","00:21:58"),
    ("00:21:58","00:22:41"),
    ("00:22:41","00:23:43"),
    ("00:23:43","00:25:29"),
]
track_info = get_track_info(soundcloud_url)
track_title = sanitize_title(track_info['title'])
output_dir = os.path.join("D:\\", "Music", "IDs", track_title)
os.makedirs(output_dir, exist_ok=True)
full_audio_path = os.path.join(output_dir, f"{track_title}_full")
download_command = [
    "yt-dlp",
    "-f", "bestaudio",
    "--add-header", "Authorization: OAuth 2-297366-66593390-stm0iYhYizqlnyA",
    soundcloud_url,
    "-o", full_audio_path,
    "--extract-audio",
    "--audio-format", "wav"
]
subprocess.call(download_command)

full_audio_path = f"{full_audio_path}.wav"
for i, (ss, to) in enumerate(timestamps, start=1):
    snippet_output_file = os.path.join(output_dir, f"{ss.replace(':', '')}-{to.replace(':', '')}")
    create_snippet(full_audio_path, ss, to, snippet_output_file)
os.remove(full_audio_path)
os.startfile(output_dir)