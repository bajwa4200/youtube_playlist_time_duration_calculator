# YouTube Playlist Duration Calculator

This Python script calculates the total duration of all videos in a specified YouTube playlist using the YouTube Data API v3.

## Features

- Retrieves all video durations from a specified YouTube playlist.
- Calculates the total duration in a human-readable format (days, hours, minutes, and seconds).

## Prerequisites

- Python 3.x
- A YouTube Data API v3 key

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/bajwa4200/youtube_playlist_time_duration_calculator.git
    cd youtube-playlist-duration-calculator
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install the required packages**:
    ```bash
    pip install google-api-python-client
    ```

4. **Set up your YouTube Data API key**:
    - Go to the [Google Developers Console](https://console.developers.google.com/), create a new project, and enable the YouTube Data API v3, then go to credentials page.
    - Create an API key and copy it.

## Usage

1. **Edit the script to include your API key and playlist ID**:
    - Open `youtube_playlist.py`.
    - Replace `"YOUR_API_KEY"` with your actual API key.
    - Replace `playlist_id = "YOUR_PLAYLIST_ID"` with the ID of the playlist you want to analyze.
    - example in this playlist link https://youtube.com/playlist?list=PL1y8hJl4KWcSZgckZpQj8cuOp1Mxnl5AC&si=VlZv4S0y4A2_XzdQ .
    - "PL1y8hJl4KWcSZgckZpQj8cuOp1Mxnl5AC&si=VlZv4S0y4A2_XzdQ" this is the playlist id.
2. **Run the script**:
    ```bash
    python3 youtube_playlist.py
    ```

3. **View the result**:
    - The script will output the total duration of the playlist in the format (e.g)`1 day, 2:02:55`.

## Example Output
  - Total Duration: 1 day, 2:02:55
## Contributions

- Feel free to submit issues or pull requests if you have suggestions for improvements!

