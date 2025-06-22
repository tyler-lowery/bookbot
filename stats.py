def count_words(text: str) -> int:
    return len(text.split())


def count_chars(text: str) -> dict[str, int]:
    char_counts = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in char_counts:
            char_counts[char_lower] += 1
        else:
            char_counts[char_lower] = 1
    return char_counts
