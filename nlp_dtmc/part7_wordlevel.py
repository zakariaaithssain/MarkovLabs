"""
Part 7: Word-Level Model (Bonus)
Treat words as tokens instead of characters.

Classes: IIA, IDF, 2SCL (2025-2026) - Optional
"""

from collections import Counter, defaultdict
import random


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
    pass


def build_word_model(tokens: list) -> dict:
    """
    Build Markov model over words (bigram model).
    
    Similar to character model but vocabulary is much larger.
    Sparsity is a major issue - most word pairs never seen.
    """
    # YOUR CODE HERE
    pass


def generate_words(model: dict, max_words: int = 50) -> str:
    """
    Generate text word by word.
    
    Usually produces more coherent but more repetitive text
    due to limited vocabulary and sparse transitions.
    """
    # YOUR CODE HERE
    pass


def main():
    print("Word-level Markov model - bonus implementation.")
    print("Compare character vs. word level:")
    print("- Character: Large samples, gibberish locally, infinite vocabulary")
    print("- Word: Small samples, coherent locally, limited vocabulary")


if __name__ == "__main__":
    main()