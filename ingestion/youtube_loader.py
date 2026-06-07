import re
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url):
    """
    Extract video ID from various YouTube URL formats
    """

    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"

    match = re.search(pattern, url)

    if match:
        return match.group(1)

    return url


def load_transcript(url):
    video_id = extract_video_id(url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = " ".join([t["text"] for t in transcript])
    return text