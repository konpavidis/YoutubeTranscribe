import youtube_transcript_api
import speech_recognition as sr
import youtube_dl
#gitpush123!!@#

def transcribe_youtube_video(video_url):
    try:
        
        try:
            transcript = youtube_transcript_api.YouTubeTranscriptApi.get_transcript(video_url)
            text = ' '.join([entry['text'] for entry in transcript])
            return text
        except youtube_transcript_api.TranscriptsDisabled:
            print("Subtitles are not available for this video.")

        
        ydl_opts = {'format': 'bestaudio', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav'}]}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            audio_url = info_dict.get('url')

        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_url) as source:
            audio_data = recognizer.record(source)
        transcription = recognizer.recognize_google(audio_data)
        return transcription
    except Exception as e:
        print("An error occurred:", str(e))
        return None



video_url = "https://www.youtube.com/watch?v=a5aPe7z8fnE&ab_channel=Shikorina100"
transcription = transcribe_youtube_video(video_url)
if transcription:
    print("Transcription:")
    print(transcription)
