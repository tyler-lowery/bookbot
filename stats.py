def count_words(text: str) -> int:
    return len(text.split())


def count_chars(text: str) -> dict[str, int]:
    char_counts = {}
    for char in text:
        c = char.lower()
        if char_lower in char_counts:
            char_counts[c] += 1
        else:
            char_counts[c] = 1
    return char_counts


def sort_char_counts_on(item):
    return item["num"]


def get_sorted_char_counts(raw_char_counts: dict[str, int]) -> list[dict[str, int | str]]:
    return sorted(
            [{"char": c, "num": n} for c, n in raw_char_counts.items()],
            key=sort_char_counts_on,
            reverse=True
        )
