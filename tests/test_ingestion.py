from ingestion.youtube_loader import load_transcript


def test_transcript_loading():

    text = load_transcript("aircAruvnKk")

    assert text is not None

    assert len(text) > 1000