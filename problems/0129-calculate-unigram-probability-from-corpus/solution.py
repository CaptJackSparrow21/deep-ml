def unigram_probability(corpus: str, word: str) -> float:
    tokens = corpus.split()
    return round(tokens.count(word) / len(tokens), 4)