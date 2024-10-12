import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yt_dlp
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Spotify API credentials
SPOTIPY_CLIENT_ID = '2a28e6c3f97c4ff1ac0d9f170b7a023b'
SPOTIPY_CLIENT_SECRET = '1372c49c07b34b6b82d6f6e330b4e68f'

# Initialize Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,client_secret=SPOTIPY_CLIENT_SECRET))

def get_spotify_playlist_tracks(playlist_url):
    try:
        results = sp.playlist_tracks(playlist_url)
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])
        return tracks
    except Exception as e:
        logging.error(f"Error retrieving Spotify playlist: {e}")
        return []

def find_soundcloud_track(track_name, artist_name):
    query = f"{track_name} {artist_name} site:soundcloud.com"
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
        'force_generic_extractor': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            search_result = ydl.extract_info(f"ytsearch:{query}", download=False)
            if search_result and 'entries' in search_result and len(search_result['entries']) > 0:
                for entry in search_result['entries']:
                    if 'soundcloud.com' in entry['url']:
                        return entry['url']
    except Exception as e:
        logging.error(f"Error searching SoundCloud for {track_name} by {artist_name}: {e}")
    return None

def main(spotify_playlist_url):
    tracks = get_spotify_playlist_tracks(spotify_playlist_url)
    if not tracks:
        logging.error("No tracks found in the Spotify playlist.")
        return

    for item in tracks:
        track = item['track']
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        soundcloud_url = find_soundcloud_track(track_name, artist_name)
        if soundcloud_url:
            logging.info(f"Spotify Track: {track_name} by {artist_name}")
            logging.info(f"SoundCloud URL: {soundcloud_url}\n")
        else:
            logging.warning(f"No SoundCloud track found for {track_name} by {artist_name}")

if __name__ == "__main__":
    spotify_playlist_url = "https://open.spotify.com/playlist/7wE0dHDpngi8UPjNhXqmGD"
    main(spotify_playlist_url)
