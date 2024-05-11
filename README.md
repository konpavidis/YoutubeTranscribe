# YouTube Video Transcription

This Python script allows you to transcribe the audio from YouTube videos into text. It utilizes the YouTube Data API to fetch available transcripts or, if unavailable, extracts the audio and transcribes it using Google's Speech Recognition API.

## Features

- Transcribes audio from YouTube videos into text.
- Utilizes YouTube Data API and Google's Speech Recognition API.
- Handles cases where subtitles are not available by extracting audio and transcribing it directly.

## Installation

1. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
2. Install the required Python packages using pip:
  pip install youtube_transcript_api
  pip install SpeechRecognition
  pip install youtube_dl

## Usage

1. Provide the URL of the YouTube video you want to transcribe by setting the `video_url` variable in the script.
2. Run the script.
  python transcribe_youtube_video.py

## Notes
-Ensure that you have the necessary permissions to access the YouTube videos you want to transcribe.
-Keep in mind that Google's Speech Recognition API has usage limits and may incur charges beyond a certain threshold.


## Credits
This script utilizes the following libraries:

- youtube_transcript_api by jdepoix
- SpeechRecognition by Uberi
- youtube_dl by ytdl-org

## Contributors

- Konstantinos Pavlakis (https://github.com/konpavidis)
