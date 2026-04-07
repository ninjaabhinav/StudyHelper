import re


def normalize_text(text):

    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def limit_context(text, max_chars=15000):

    return text[:max_chars]


def split_into_blocks(text, size=5000):

    blocks = []

    for i in range(0, len(text), size):
        blocks.append(text[i:i + size])

    return blocks