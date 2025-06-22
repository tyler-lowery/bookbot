from stats import count_words, count_chars


def get_book_text(book_file: str) -> str:
    with open(book_file) as f:
        file_contents = f.read()
    return file_contents


def main() -> None:
    #print(get_book_text(book_file="./books/frankenstein.txt"))
    book_text = get_book_text(book_file="./books/frankenstein.txt")
    num_words = count_words(text=book_text)
    char_counts = count_chars(text=book_text)
    print(f"{num_words} words found in the document")
    print(char_counts)


if __name__ == "__main__":
    main()
