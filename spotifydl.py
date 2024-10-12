import subprocess
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Spotify playlist URL
url = 'https://open.spotify.com/track/6XJi6FR7DekN9WvgNhQ9No'

# Command to extract metadata without downloading
command = [
    "spotify_dl",
    "--url", url,
    "-o", r"D:\Music",
]

# Execute the command
subprocess.call(command)

os.startfile(r"D:\Music")
