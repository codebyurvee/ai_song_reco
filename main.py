from data import songs


def clean_text(text):
    text = text.lower()
    text = text.replace("-", " ").replace(",", " ")
    text = " ".join(text.split())
    return text.split()


def get_vocabulary(songs):
    vocab = set()
    for song in songs:
        vocab.update(clean_text(song["genres"]))
        vocab.update(clean_text(song["mood"]))
    return sorted(list(vocab))


def text_to_vector(text, vocabulary):
    words = clean_text(text)
    vector = [0] * len(vocabulary)
    for word in words:
        if word in vocabulary:  # safety
            index = vocabulary.index(word)
            vector[index] += 1
    return vector


# Cosine Similarity
def cosine(vec1, vec2):
    dot = sum(a * b for a, b in zip(vec1, vec2))
    mag1 = (sum(a * a for a in vec1)) ** 0.5
    mag2 = (sum(b * b for b in vec2)) ** 0.5
    return dot / (mag1 * mag2) if mag1 * mag2 != 0 else 0


# Build vectors
vocabulary = get_vocabulary(songs)
song_vectors = [text_to_vector(song["genres"] + " " + song["mood"], vocabulary) for song in songs]


def recommend_by_song(song_index, top_n=3):
    target = song_vectors[song_index]
    scores = []

    for i in range(len(song_vectors)):
        if i != song_index:
            sim = cosine(target, song_vectors[i])
            scores.append((i, sim))

    scores.sort(key=lambda x: x[1], reverse=True)

    print(f"\n🎵 Songs similar to: {songs[song_index]['title']}\n")
    for i in range(top_n):
        idx, score = scores[i]
        print(f"{songs[idx]['title']} - {songs[idx]['artist']}")
        print(f"Similarity: {score:.2f}\n")


# Call it
recommend_by_song(1, top_n=5)  # Levitating ke similar songs