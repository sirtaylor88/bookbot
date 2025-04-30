"""Module defining methods to get stats."""

import re
from collections import defaultdict


def get_num_words(document: str) -> int:
    """Return the number of words in the document.

    Args:
        document: A string.

    Returns:
        An integer.
    """
    document = re.sub(r"\s", " ", document)
    return len(document.split())


def get_num_chars(document: str) -> dict[str, int]:
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
            result[c] += 1

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
