from collections import defaultdict

def count_words(document: str) -> int:
    """Return the number of words in the document.
    
    Args:
        document: A string.
    
    Returns:
        An integer.
    """
    return len(document.split())

def count_chars(document: str) -> dict[str, int]:
    """Return the number of chars
      in the document.
    
    Args:
        document: A string.
    
    Returns:
        A dict mapping character to its occurences.
    """
    words = document.lower().split()
    result = defaultdict(lambda: 0)
                         
    for word in words:
        for c in word:
            result[c] +=1

    return dict(result)

def sort_chars(chars_dict: dict[str, int]) -> list[dict]:
    """Sort chars statistics by descending order.

    Args:
        chars_dict: A dict mapping character to its occurences.
    
    Returns:
        A list of dict with the following structure:
            { "name": "a", "count": 123 }
    """
    new_list = [{"name": k, "count": v} for k, v in chars_dict.items()]
    return sorted(new_list, key=lambda x: x["count"], reverse=True)

def report(filepath: str) -> str:
    """Build a report about the book.

    Args:
        filepath: A file path to book.
    
    Returns:
        A text report.
    """

    try:
        with open(filepath) as f:
            file_content = f.read()
    except IOError:
        return "Cannot create report: Wrong file path !"

    text = f"--- Begin report of {filepath} ---\n"
    text += f"{count_words(file_content)} words found in the document\n\n"
    for item in sort_chars(count_chars(file_content)):
        if item["name"].isalpha():
            text += (
                f"""The '{item["name"]}' character was found {item["count"]} times\n"""
            )
    return text

def main():
    book_path = "books/frankenstein.txt"
    text = report(book_path)
    num_words = count_words(text)
    chars_dict = count_chars(text)
    chars_sorted_list = sort_chars(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["name"].isalpha():
            continue
        print(f"The '{item['name']}' character was found {item['count']} times")

    print("--- End report ---")

main()