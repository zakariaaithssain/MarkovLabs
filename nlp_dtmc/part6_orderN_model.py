"""
Part 6: Higher-Order Markov Models
Extend to context lengths > 1 (order-3, order-5, etc.)

Classes: IIA, IDF, 2SCL (2025-2026)
"""

from collections import defaultdict, Counter
from typing import Tuple, Optional
from part2_preprocessing import preprocess, VOCAB
import random

def preprocess_for_order_n(text: str, order: int) -> str:
    """
    Preprocess text for order-n model.
    
    TODO: Add 'order' start markers instead of just one.
    Example: order=3 -> "^^^text$"
    
    Args:
        text: Raw text
        order: Context length (number of previous characters)
    
    Returns:
        Preprocessed text with multiple start markers
    """
    # YOUR CODE HERE
    pass


def build_high_order_model(text: str, order: int = 3) -> dict:
    """
    Build Markov model of arbitrary order.
    
    TODO: Similar to order-1, but:
        - History is a tuple of 'order' characters, not a single char
        - Use tuple(text[i:i+order]) as dictionary key
        - Still apply Laplace smoothing
    
    Memory efficiency note: Use dictionary, not full matrix!
    Theoretical size is |V|^order (huge), but actual size is much smaller
    because most n-grams never appear in training data.
    
    Args:
        text: Raw training text
        order: Context length (1 = first-order, 3 = third-order, etc.)
    
    Returns:
        Dictionary: {history_tuple: {next_char: probability}}
    """
    # YOUR CODE HERE
    pass


def generate_high_order(model: dict, order: int = 3, 
                        max_length: int = 200, top_k: Optional[int] = None,
                        seed: Optional[int] = None) -> str:
    """
    Generate text using high-order Markov model.
    
    TODO: Similar to order-1 generation, but:
        - Start with tuple of 'order' '^' characters
        - Maintain sliding window of last 'order' characters
        - Update window: drop oldest, add newest
    
    Args:
        model: High-order probability matrix
        order: Context length used in model
        max_length: Maximum characters to generate
        top_k: Optional top-k sampling
        seed: Random seed
    
    Returns:
        Generated text
    """
    if seed is not None:
        random.seed(seed)
    
    # YOUR CODE HERE
    pass


def compare_orders(train_text: str, test_text: str, max_order: int = 5):
    """
    Compare models of different orders on the same data.
    
    This demonstrates the bias-variance tradeoff in sequence modeling.
    """
    print("="*60)
    print(f"COMPARING ORDERS 1 TO {max_order}")
    print("="*60)
    
    for order in range(1, max_order + 1):
        print(f"\nBuilding order-{order} model...")
        model = build_high_order_model(train_text, order)
        
        # Count states
        num_states = len(model)
        theoretical_states = len(VOCAB) ** order
        
        print(f"  Actual states: {num_states}")
        print(f"  Theoretical max: {theoretical_states}")
        print(f"  Sparsity: {100 * (1 - num_states/theoretical_states):.2f}%")
        
        # Quick generation sample
        sample = generate_high_order(model, order, max_length=80, seed=42)
        clean_sample = sample.replace('^', '').replace('$', '')
        print(f"  Sample: {clean_sample[:60]}...")


def main():
    print("High-order Markov models - implementation required.")
    print("This is the most challenging part of the lab.")


if __name__ == "__main__":
    main()