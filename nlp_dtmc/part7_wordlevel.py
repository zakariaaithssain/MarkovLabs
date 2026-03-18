"""
Part 7: Word-Level Model (Bonus)
Treat words as tokens instead of characters.

Classes: IIA, IDF, 2SCL (2025-2026) - Optional
"""

from collections import Counter, defaultdict
import random

from part2_preprocessing import preprocess


def tokenize(text: str, max_vocab_size: int = 1000) -> list:
    """
    Split text into words (tokens).
    
    TODO: Simple whitespace tokenization, with:
        1. Lowercasing
        2. Removing punctuation
        3. Replacing rare words with <UNK>
        4. Adding <START> and <END> markers
    
    Args:
        text: Raw text
        max_vocab_size: Keep only most frequent words
    
    Returns:
        List of tokens
    """
    # YOUR CODE HERE
    text = preprocess(text).replace("^", "<START>").replace("$", "<END>")
    words_list = text.split()

    count = Counter(words_list)
    vocab = set(sorted(count.keys(), key=lambda token: count[token], reverse=True)[:max_vocab_size])

    return [word if word in vocab else "<UNK>" for word in words_list]




def build_word_model(tokens: list) -> dict:
    """
    Build Markov model over words (bigram model).
    
    Similar to character model but vocabulary is much larger.
    Sparsity is a major issue - most word pairs never seen.
    """
    # YOUR CODE HERE
    counts = defaultdict(lambda: defaultdict(int))

    for current, next_word in zip(tokens, tokens[1:]):
        counts[current][next_word] += 1

    probs = {}
    for current, next_counts in counts.items():
        total = sum(next_counts.values())
        probs[current] = {word: count / total for word, count in next_counts.items()}

    return probs


def generate_words(model: dict, max_words: int = 50) -> str:
    """
    Generate text word by word.
    
    Usually produces more coherent but more repetitive text
    due to limited vocabulary and sparse transitions.
    """
    # YOUR CODE HERE
    current = "<START>"
    words = []
    for _ in range(max_words):
        if current not in model:
            break

        next_probs = model[current]
        chars  = list(next_probs.keys())
        weights = list(next_probs.values())
        current = random.choices(chars, weights=weights, k=1)[0]

        if current == "<END>":
            break

        words.append(current)

    return " ".join(words)


def main():
    print("Word-level Markov model - bonus implementation.")
    print("Compare character vs. word level:")
    print("- Character: Large samples, gibberish locally, infinite vocabulary")
    print("- Word: Small samples, coherent locally, limited vocabulary")


if __name__ == "__main__":
    main()