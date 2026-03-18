"""
Part 3: First-Order Markov Model
Build transition matrix with Laplace smoothing.

Classes: IIA, IDF, 2SCL (2025-2026)
"""

from collections import defaultdict, Counter
from part2_preprocessing import preprocess, VOCAB


def count_transitions(text: str) -> dict:
    """
    Count character transitions in preprocessed text.
    
    TODO: Count how often each character is followed by another.
    Use a dictionary mapping current_char -> Counter of next_chars.
    
    Example: For text "^abc$":
        '^' is followed by 'a' (count: 1)
        'a' is followed by 'b' (count: 1)
        'b' is followed by 'c' (count: 1)
        'c' is followed by '$' (count: 1)
    
    Args:
        text: Preprocessed text (with ^ and $ markers)
    
    Returns:
        Dictionary: {current_char: Counter({next_char: count})}
    """
    result = defaultdict(Counter)
    for sym in VOCAB: 
        if sym in text: 
            count_next = Counter({})
            for i in range(len(text)-1): 
                if text[i] == sym: 
                    next_char = text[i+1]
                    count_next.update({next_char: 1})
            
            result[sym] = count_next
        
    return result

def build_probability_matrix(counts: dict, vocab: list) -> dict:
    """
    Convert counts to probabilities with Laplace smoothing.
    
    TODO: For each character in vocab, compute P(next|current).
    
    Laplace smoothing formula:
        P(next|current) = (count(current->next) + 1) / (total_count(current) + vocab_size)
    
    This ensures no probability is ever zero.
    
    Args:
        counts: Transition counts from count_transitions()
        vocab: List of all possible characters
    
    Returns:
        Nested dict: {current: {next: probability}}
    """
    probs = {}
    for current in vocab: 
        next_probs = {}
        for next_char in vocab: 
            laplace = (counts[current][next_char] + 1) / (counts[current].total() + len(vocab))
            next_probs[next_char] = laplace
        
        probs[current] = next_probs
    
    return probs
        



def verify_model(model: dict, vocab: list) -> bool:
    """
    Verify that probabilities sum to 1.0 for each state.
    
    Returns True if valid, False otherwise.
    """
    is_valid = True
    for char in vocab:
        if char not in model:
            print(f"Missing entry for character: '{char}'")
            is_valid = False
            continue
        
        prob_sum = sum(model[char].values())
        if abs(prob_sum - 1.0) > 0.001:  # Allow small floating point error
            print(f"Probabilities for '{char}' sum to {prob_sum:.4f} (should be 1.0)")
            is_valid = False
    
    return is_valid


def main():
    # Test with simple example
    test_text = "^abc$"
    processed = test_text  # Already preprocessed
    
    print("Testing with:", processed)
    
    counts = count_transitions(processed)
    print("\nTransition counts:")
    for char, counter in counts.items():
        print(f"  '{char}': {dict(counter)}")
    
    model = build_probability_matrix(counts, VOCAB)
    
    print("\nVerifying model...")
    if verify_model(model, VOCAB):
        print("✓ Model is valid!")
        
        # Show some probabilities
        print("\nSample probabilities from 'a':")
        for next_char, prob in sorted(model['a'].items(), key=lambda x: -x[1])[:5]:
            if prob > 0.01:  # Only show non-trivial probabilities
                print(f"  P('{next_char}'|'a') = {prob:.4f}")
    else:
        print("✗ Model has errors. Please fix.")


if __name__ == "__main__":
    main()