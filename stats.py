def count_words(text: str) -> int:
    """Count the total number of words in the given text string.

    Returns: int
    """
    return len(text.split())


def count_chars(text: str) -> dict[str, int]:
    """Count the occurances of each character (case insenstive).

    Returns:
        dict[str, int]
            A dictionary with the format: {"char": count} (e.g., {"b": 25})
    """
    char_counts = {}
    for char in text:
        c = char.lower()
        if c in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1
    return char_counts


def sort_char_counts_on(item):
    """Sort char counts on the integer count."""
    return item["num"]


def get_sorted_char_counts(raw_char_counts: dict[str, int]) -> list[dict[str, int | str]]:
    """Return a sorted list of characters and their counts.

    Args:
        raw_char_counts: dict[str, int]
            A dictionary with the format: {"char": count} (e.g., {"b", 25})

    Returns:
        list[dict[str, int | str]]
            A list of dictionaries of the form {"char": "b", "num": 25}
    """
    return sorted(
            [{"char": c, "num": n} for c, n in raw_char_counts.items()],
            key=sort_char_counts_on,
            reverse=True
        )
