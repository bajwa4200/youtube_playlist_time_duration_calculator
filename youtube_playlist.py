import os
import re

import googleapiclient.discovery
from datetime import timedelta

# Replace with your API key
api_key = "YOUR_API_KEY"

# Replace with your playlist ID
playlist_id = "YOUR_PLAYLIST_ID"

# Set up the YouTube API client
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

def get_playlist_videos(playlist_id):
    videos = []
    next_page_token = None

    while True:
        pl_request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        pl_response = pl_request.execute()

        videos += pl_response["items"]

        next_page_token = pl_response.get("nextPageToken")

        if next_page_token is None:
            break

    return videos

def get_video_durations(video_ids):
    durations = []
    for i in range(0, len(video_ids), 50):
        video_request = youtube.videos().list(
            part="contentDetails",
            id=",".join(video_ids[i:i + 50])
        )
        video_response = video_request.execute()

        for item in video_response["items"]:
            duration = item["contentDetails"]["duration"]
            durations.append(duration)

    return durations

def parse_duration(duration):
    parsed_duration = timedelta()
    try:
        hours = int(re.search(r'(\d+)H', duration).group(1))
    except AttributeError:
        hours = 0
    try:
        minutes = int(re.search(r'(\d+)M', duration).group(1))
    except AttributeError:
        minutes = 0
    try:
        seconds = int(re.search(r'(\d+)S', duration).group(1))
    except AttributeError:
        seconds = 0

    parsed_duration += timedelta(hours=hours, minutes=minutes, seconds=seconds)
    return parsed_duration

# Get the videos in the playlist
videos = get_playlist_videos(playlist_id)

# Get the video IDs
video_ids = [video["contentDetails"]["videoId"] for video in videos]

# Get the durations of the videos
durations = get_video_durations(video_ids)

# Calculate the total duration
total_duration = sum([parse_duration(duration) for duration in durations], timedelta())

print("Total Duration: ", total_duration)

