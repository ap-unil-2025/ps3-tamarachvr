"""
Problem 4: File Word Counter
Process text files and perform various analyses.
"""

def create_sample_file(filename="sample.txt"):
    """
    Create a sample text file for testing.

    Args:
        filename (str): Name of the file to create
    """
    content = """Python is a powerful programming language.
It is widely used in web development, data science, and automation.
Python's simple syntax makes it great for beginners.
Many companies use Python for their projects."""

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(content)
    print(f"Created {filename}")


def count_words(filename):
    """Return total number of words in the file."""
    with open(filename, "r", encoding="utf-8") as f:
        return len(f.read().split())


def count_lines(filename):
    """Return total number of lines in the file."""
    with open(filename, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def count_characters(filename, include_spaces=True):
    """Return number of characters in the file."""
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    if not include_spaces:
        text = text.replace(" ", "")
    return len(text)


def find_longest_word(filename):
    """Return the longest word (punctuation stripped)."""
    import string
    with open(filename, "r", encoding="utf-8") as f:
        words = f.read().split()
    table = str.maketrans("", "", string.punctuation)
    words = [w.translate(table) for w in words if w.translate(table)]
    return max(words, key=len) if words else ""


def word_frequency(filename):
    """Return dict: word -> count (lowercased, punctuation removed)."""
    import string
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read().lower()
    table = str.maketrans("", "", string.punctuation)
    words = [w.translate(table) for w in text.split() if w.translate(table)]
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


def analyze_file(filename):
    """
    Perform complete analysis of the file.

    Args:
        filename (str): Name of the file to analyze
    """
    print(f"\nAnalyzing: {filename}")
    print("-" * 40)

    try:
        # Display all analyses
        print(f"Lines: {count_lines(filename)}")
        print(f"Words: {count_words(filename)}")
        print(f"Characters (with spaces): {count_characters(filename, True)}")
        print(f"Characters (without spaces): {count_characters(filename, False)}")
        print(f"Longest word: {find_longest_word(filename)}")

        # Display top 5 most common words
        print("\nTop 5 most common words:")
        freq = word_frequency(filename)
        top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
        for word, count in top_words:
            print(f"  '{word}': {count} times")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function to run the file analyzer."""
    # Create sample file
    create_sample_file()

    # Analyze the sample file
    analyze_file("sample.txt")

    # Allow user to analyze their own file
    print("\n" + "=" * 40)
    user_file = input("Enter a filename to analyze (or press Enter to skip): ").strip()
    if user_file:
        analyze_file(user_file)


if __name__ == "__main__":
    main()