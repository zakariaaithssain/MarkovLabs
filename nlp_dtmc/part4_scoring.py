"""
Part 4: Model Evaluation
Compute log-likelihood and perplexity.

Classes: IIA, IDF, 2SCL (2025-2026)
"""

import math
from part2_preprocessing import preprocess, VOCAB


def compute_log_likelihood(model: dict, test_text: str) -> float:
    """
    Compute log-likelihood of test text under the model.
    
    TODO: Implement log-likelihood calculation:
        log_likelihood = sum(log(P(char_{i+1} | char_i)))
    
    IMPORTANT: Use math.log() for each probability, then sum.
    Do NOT sum probabilities directly!
    
    For unseen transitions, use uniform probability: 1/|V|
    
    Args:
        model: Probability matrix from build_probability_matrix()
        test_text: Raw test string (will be preprocessed)
    
    Returns:
        Log-likelihood value (negative float)
    """
    # Preprocess test text
    text = preprocess(test_text)
    
    # YOUR CODE HERE
    pass


def compute_perplexity(log_likelihood: float, n_transitions: int) -> float:
    """
    Compute perplexity from log-likelihood.
    
    TODO: Implement: perplexity = exp(-log_likelihood / n)
    
    Perplexity can be interpreted as the "effective vocabulary size"
    - Lower is better
    - Random guessing would give perplexity = |V| = 29
    - Perfect prediction would give perplexity = 1
    """
    # YOUR CODE HERE
    pass


def evaluate_model(model: dict, train_text: str, test_same: str, test_diff: str):
    """
    Comprehensive evaluation comparing train vs. test performance.
    
    This demonstrates overfitting detection - a crucial skill in ML.
    """
    print("="*60)
    print("MODEL EVALUATION")
    print("="*60)
    
    # Training text (should fit well, but not perfectly due to smoothing)
    ll_train = compute_log_likelihood(model, train_text)
    n_train = len(preprocess(train_text)) - 1
    ppl_train = compute_perplexity(ll_train, n_train)
    
    print(f"\nTraining text:")
    print(f"  Log-likelihood: {ll_train:.2f}")
    print(f"  Avg log-likelihood: {ll_train/n_train:.4f}")
    print(f"  Perplexity: {ppl_train:.2f}")
    
    # Same style test (should be similar to train)
    ll_same = compute_log_likelihood(model, test_same)
    n_same = len(preprocess(test_same)) - 1
    ppl_same = compute_perplexity(ll_same, n_same)
    
    print(f"\nTest text (same style):")
    print(f"  Log-likelihood: {ll_same:.2f}")
    print(f"  Avg log-likelihood: {ll_same/n_same:.4f}")
    print(f"  Perplexity: {ppl_same:.2f}")
    
    # Different style (should be worse = higher perplexity)
    ll_diff = compute_log_likelihood(model, test_diff)
    n_diff = len(preprocess(test_diff)) - 1
    ppl_diff = compute_perplexity(ll_diff, n_diff)
    
    print(f"\nTest text (different style/language):")
    print(f"  Log-likelihood: {ll_diff:.2f}")
    print(f"  Avg log-likelihood: {ll_diff/n_diff:.4f}")
    print(f"  Perplexity: {ppl_diff:.2f}")
    
    print(f"\n" + "="*60)
    print("ANALYSIS:")
    if ppl_same < ppl_diff:
        print("✓ Model correctly assigns lower perplexity to similar text")
    else:
        print("✗ Unexpected: different text has lower perplexity")
    print("="*60)


def main():
    # This will be tested with real data in the full pipeline
    # For now, create a dummy model for testing
    dummy_model = {
        c: {n: 1/29 for n in VOCAB}  # Uniform distribution
        for c in VOCAB
    }
    
    # Test log-likelihood computation
    test_text = "hello"
    ll = compute_log_likelihood(dummy_model, test_text)
    n = len(preprocess(test_text)) - 1
    ppl = compute_perplexity(ll, n)
    
    print(f"Test with uniform model:")
    print(f"  Text: '{test_text}'")
    print(f"  Log-likelihood: {ll:.4f}")
    print(f"  Perplexity: {ppl:.2f} (should be ~29 for uniform model)")


if __name__ == "__main__":
    main()