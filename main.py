from stats import count_words, count_chars, get_sorted_char_counts


def get_book_text(book_file: str) -> str:
    with open(book_file) as f:
        return f.read()


def print_report(
        path_to_book: str,
        num_words: int,
        sorted_char_counts: list[dict[str, int | str]]
        ) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_char_counts:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def main() -> None:
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(book_file=path_to_book)
    num_words = count_words(text=book_text)
    char_counts = count_chars(text=book_text)
    sorted_char_counts = get_sorted_char_counts(raw_char_counts=char_counts)
    print_report(path_to_book, num_words, sorted_char_counts)


if __name__ == "__main__":
    main()
