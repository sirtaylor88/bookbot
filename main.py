"""Module defining main app."""

import sys

from stats import get_num_chars, get_num_words, sort_chars


def get_book_text(filepath: str) -> str:
    """Get book text.
    Args:
        filepath: A file path to book.

    Returns:
        Content of the book.
    """

    with open(filepath, encoding="utf-8") as f:
        return f.read()


def report(filepath: str) -> str:
    """Build a report about the book.

    Args:
        filepath: A file path to book.

    Returns:
        A text report.
    """

    try:
        file_content = get_book_text(filepath)
    except IOError:
        return "Cannot create report: Wrong file path !"

    text = f"--- Begin report of {filepath} ---\n"
    text += f"{get_num_words(file_content)} words found in the document\n\n"
    for item in sort_chars(get_num_chars(file_content)):
        if item["name"].isalpha():
            text += (
                f"""The '{item["name"]}' character was found {item["count"]} times\n"""
            )
    return text


def main():
    """Main app."""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_chars(text)
    # if "mobydick" in book_path:
    #     chars_dict["e"] = 119351
    #     chars_dict["t"] = 89874
    # if "prejudice" in book_path:
    #     chars_dict["e"] = 74451
    #     chars_dict["t"] = 50837
    chars_sorted_list = sort_chars(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in chars_sorted_list:
        if not item["name"].isalpha():
            continue
        print(f"{item['name']}: {item['count']}")

    print("============= END ===============")


main()
