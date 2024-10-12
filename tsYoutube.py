import subprocess
import os
import json

# Function to get video metadata
def get_video_info(video_id):
    return json.loads(subprocess.run(
        ["yt-dlp", f"https://www.youtube.com/watch?v={video_id}", "-J"],
        capture_output=True,
        text=True
    ).stdout)

# Function to sanitize the title for file system compatibility
def sanitize_title(title):
    return "".join([c if c.isalnum() else "_" for c in title])

# Video details
video_id = "Sou3sOHDRak"
ss = "00:01:24"
to = "00:02:09"

# Get video info
video_info = get_video_info(video_id)
video_title = sanitize_title(video_info['title'])

# Construct output path
output_dir = os.path.join("D:\\", "Music", "IDs")
os.makedirs(output_dir, exist_ok=True)
output = os.path.join(output_dir, f"{video_title}.wav")

# yt-dlp command
download_command = [
    "yt-dlp",
    "-f", "bestaudio",
    f"https://www.youtube.com/watch?v={video_id}",
    "-o", output,
    "--extract-audio",
    "--audio-format", "wav",
    "--postprocessor-args", f"ffmpeg:-ss {ss} -to {to}"
]

# Run the download command
subprocess.call(download_command)
os.startfile(output_dir)