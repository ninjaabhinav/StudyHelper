import re
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return url

def load_transcript(url):
    video_id = extract_video_id(url)
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([t["text"] for t in transcript])
        return text
    except TranscriptsDisabled:
        raise Exception("This video has transcripts disabled. Please try a different video.")
    except NoTranscriptFound:
        raise Exception("No English transcript found for this video.")
    except Exception as e:
        raise Exception(f"Could not fetch transcript: {str(e)}")