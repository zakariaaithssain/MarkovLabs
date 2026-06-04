"""
Part 5: Text Generation
Generate new text by sampling from the Markov model.

Classes: IIA, IDF, 2SCL (2025-2026)
"""

import random
from typing import Optional, Dict
from collections import Counter
from part2_preprocessing import VOCAB



def sample_from_distribution(prob_dist: Dict[str, float], top_k: Optional[int] = None) -> str:
    """
    Sample a character from a probability distribution.
    
    TODO: Implement sampling:
        1. If top_k is specified, keep only k most likely chars and renormalize
        2. Use random.choices() with weights to sample
    
    Args:
        prob_dist: Dictionary {char: probability}
        top_k: If set, sample only from top k most probable characters
    
    Returns:
        Sampled character
    """
    # YOUR CODE HERE
    if top_k: 
        kept_prob = dict(
            sorted(prob_dist.items(),
                    key= lambda x: x[1],
                    reverse=True)[:top_k]
                      )
        #normalization
        total = sum(kept_prob.values())
        prob_dist = {char : (prob/ total) for char, prob in kept_prob.items()}
    
    return random.choices(population=list(prob_dist.keys()),
                           weights= list(prob_dist.values()),
                            k=1)[0]


def generate_text(model: dict, max_length: int = 200, 
                  top_k: Optional[int] = None, seed: Optional[int] = None) -> str:
    """
    Generate text using first-order Markov model.
    
    TODO: Implement generation algorithm:
        1. Start with '^'
        2. While not reached max_length and not generated '$':
           a. Get probability distribution for current character
           b. Sample next character
           c. Append to result
           d. Update current character
        3. Return generated string (including markers or clean, your choice)
    
    Args:
        model: Probability matrix
        max_length: Maximum characters to generate
        top_k: Optional restriction to top-k sampling
        seed: Random seed for reproducibility
    
    Returns:
        Generated text string
    """
    if seed is not None:
        random.seed(seed)
    
    # YOUR CODE HERE
    result = ""
    current_char= "^"
    while max_length > 0 : 
        prob_dist = model[current_char]
        next_char = sample_from_distribution(prob_dist, top_k)
        if next_char == "$": 
         break

        result+= next_char
        current_char = next_char
        max_length -= 1

def compare_sampling_strategies(model: dict, num_samples: int = 3):
    """
    Compare different sampling strategies.
    
    This helps understand the creativity vs. coherence trade-off.
    """
    print("="*60)
    print("SAMPLING STRATEGY COMPARISON")
    print("="*60)
    
    strategies = [
        (None, "Full sampling (diverse, sometimes weird)"),
        (10, "Top-10 (balanced)"),
        (5, "Top-5 (more conservative)"),
        (1, "Greedy (deterministic, repetitive)"),
    ]
    
    for top_k, description in strategies:
        print(f"\n{description}:")
        print("-" * 40)
        for i in range(num_samples):
            generated = generate_text(model, max_length=100, top_k=top_k, seed=42+i)
            # Clean up for display
            clean = generated.replace('^', '').replace('$', '')
            print(f"  {i+1}. {clean}")


def main():
    print("This module requires a trained model from part3.")
    print("Run the full pipeline (main.py) to test generation.")
    
    # Demonstrate sampling with dummy uniform distribution
    dummy_dist = {c: 1/29 for c in VOCAB}
    
    print("\nDemonstrating sampling from uniform distribution:")
    samples = [sample_from_distribution(dummy_dist) for _ in range(20)]
    print("Samples:", ''.join(samples))


if __name__ == "__main__":
    main()