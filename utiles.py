from data import songs


def clean_text(text):
    text = text.lower()
    text = text.replace("-", " ")
    text = text.replace(",", " ")
    text = text.strip()
    text = text = " ".join(text.split())
    return text.split()


def get_vocabulary(songs):
    vocab = set()
    for song in songs:
        genres_words = clean_text(song["genres"])
        mood_words = clean_text(song["mood"])
        vocab.update(genres_words)
        vocab.update(mood_words)
    return sorted(list(vocab))


def text_to_vector(text, vocabulary):
    words = clean_text(text)
    vector = [0] * len(vocabulary)
    for word in words:
        index = vocabulary.index(word)
        vector[index] = vector[index] + 1
    return vector