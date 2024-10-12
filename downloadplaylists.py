import subprocess
import os
import json

def fetch_playlists(user_url):
    fetch_command = [
        "yt-dlp",
        "--flat-playlist",
        "--dump-json",
        user_url
    ]
    result = subprocess.run(fetch_command, capture_output=True, text=True)
    output_lines = result.stdout.strip().split('\n')
    playlists = [json.loads(line) for line in output_lines if f"{user_url}/sets/" in json.loads(line).get('url', '')]
    return playlists

def download_playlist_tracks(playlist_url, playlist_title, output_dir):
    folder_name = "".join(x if x.isalnum() else "_" for x in playlist_title)
    playlist_folder = os.path.join(output_dir, folder_name)
    os.makedirs(playlist_folder, exist_ok=True)
    
    print(f"Downloading playlist: {playlist_title} into {playlist_folder}")
    
    download_command = [
        "yt-dlp",
        "-f", "bestaudio",
        "--add-header", "Authorization: OAuth 2-297366-66593390-stm0iYhYizqlnyA",
        playlist_url,
        "-o", os.path.join(playlist_folder, "%(title)s.%(ext)s"),
        "--extract-audio",
        "--audio-format", "wav"
    ]
    subprocess.run(download_command)

if __name__ == '__main__':
    soundcloud_user_url = "https://soundcloud.com/pippavicera"
    output_directory = os.path.join("D:\\", "Music", "Pippa")
    for playlist in fetch_playlists(soundcloud_user_url):
        playlist_title = playlist.get('title', 'Untitled Playlist')
        playlist_url = playlist.get('url')
        download_playlist_tracks(playlist_url, playlist_title, output_directory)
    
    os.startfile(output_directory)
