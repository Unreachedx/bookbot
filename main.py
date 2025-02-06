def count_words(text):
    """Counts the number of words in a given text string."""
    words = text.split()
    return len(words)

def count_characters(text):
    """Counts occurrences of each alphabetic character in the text."""
    char_counts = {}
    text = text.lower()
    
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            char_counts[char] = char_counts.get(char, 0) + 1
         
    return char_counts

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)

    # Generate the report
    print("\n--- Book Report ---\n")
    print(f"Total word count: {word_count}\n")
    print("Character counts:\n")
    
    for char, count in sorted(char_count.items()):  # Sort alphabetically
        print(f"The '{char}' character was found {count} times")
    
    print("\n--- End of Report ---\n")

main()
