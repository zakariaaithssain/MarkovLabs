"""
Part 2: Text Preprocessing
Clean and normalize text for Markov chain modeling.

Classes: IIA, IDF, 2SCL (2025-2026)
"""

# Vocabulary definition: 29 characters total
# Space + 26 letters + start marker ^ + end marker $
import re


VOCAB = ['^', '$', ' '] + list('abcdefghijklmnopqrstuvwxyz')
VOCAB_SIZE = len(VOCAB)  # Should be 29


def preprocess(text: str) -> str:
    """
    Preprocess raw text for Markov modeling.
    
    TODO: Implement the preprocessing pipeline:
        1. Convert to lowercase
        2. Keep only allowed characters (a-z and space)
        3. Add '^' at the beginning and '$' at the end
    
    Example:
        "Hello World!" -> "^hello world$"
        "ABC 123 xyz" -> "^abc xyz$"
    
    Args:
        text: Raw input string
    
    Returns:
        Processed string with markers
    
    Raises:
        ValueError: If result is empty (no valid characters in input)
    """
    # YOUR CODE HERE

    text = text.lower()
    text = ''.join(c for c in text if c in 'abcdefghijklmnopqrstuvwxyz ')
    text = re.sub(r' {2,}', ' ', text)  #collapse multiple spaces into one

    if text.strip():
        return "^" + text + "$" 
    else: 
        raise ValueError("no valid characters in input")
    


def validate_preprocessing():
    """Test cases for preprocessing function."""
    test_cases = [
        ("Hello World!", "^hello world$"),
        ("ABC 123 xyz", "^abc xyz$"),
        ("   Spaces   ", "^ spaces $"),
        ("UPPER lower", "^upper lower$"),
    ]
    
    all_passed = True
    for input_text, expected in test_cases:
        result = preprocess(input_text)
        if result == expected:
            print(f"✓ PASS: '{input_text}' -> '{result}'")
        else:
            print(f"✗ FAIL: '{input_text}'")
            print(f"  Expected: '{expected}'")
            print(f"  Got:      '{result}'")
            all_passed = False
    
    # Test empty input
    try:
        preprocess("!@#$%^&*()")
        print("✗ FAIL: Should raise ValueError for empty result")
        all_passed = False
    except ValueError:
        print("✓ PASS: Correctly raises ValueError for empty result")
    
    return all_passed


def main():
    if validate_preprocessing():
        print("\n" + "="*50)
        print("All tests passed! You can proceed.")
        print("="*50)
    else:
        print("\n" + "="*50)
        print("Some tests failed. Please fix your implementation.")
        print("="*50)


if __name__ == "__main__":
    main()