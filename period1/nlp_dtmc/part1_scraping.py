"""
Part 1: Data Acquisition
Fetch text from web sources for Markov chain training.

Classes: IIA, IDF, 2SCL (2025-2026)
"""

import requests
from bs4 import BeautifulSoup


def fetch_text(url: str, max_chars: int = 10000) -> str:
    """
    Fetch text content from a URL.
    
    Handles both plain text (.txt) and HTML pages.
    For HTML, extracts text from <p> tags.
    
    TODO: Implement this function
    Steps:
        1. Send HTTP GET request
        2. Check status code (200 = success)
        3. If content starts with '<', it's HTML -> parse with BeautifulSoup
        4. Otherwise, it's plain text -> use directly
        5. Return first max_chars characters
    
    Args:
        url: Web address to fetch
        max_chars: Maximum characters to return (for performance)
    
    Returns:
        Extracted text string
    
    Raises:
        Exception: If HTTP request fails
    """
    # YOUR CODE HERE
    response = requests.get(url)
    if response.status_code == 200: 
        if response.text.startswith("<"): 
            bs = BeautifulSoup(response.text, "html.parser")
            p_tags = bs.find_all("p")
            txt = ""
            for parag in p_tags: 
                txt += parag.text.strip()
        else: 
            txt = response.text
        
        return txt[:max_chars]
    else: 
        raise requests.HTTPError
    

def main():
    # Test URLs - choose one:
    # English: "https://www.gutenberg.org/files/1342/1342-0.txt" (Pride and Prejudice)
    # French: "https://www.gutenberg.org/files/14155/14155-0.txt" (Le Rouge et le Noir)
    
    test_url = "https://www.gutenberg.org/files/1342/1342-0.txt"
    
    try:
        text = fetch_text(test_url, max_chars=5000)
        print(f"Successfully fetched {len(text)} characters")
        print(f"Preview: {text}...")
        return text
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    main()