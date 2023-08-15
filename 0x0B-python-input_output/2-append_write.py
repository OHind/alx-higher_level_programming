#!/usr/bin/python3
"""Append a line"""


def append_write(filename="", text=""):
    """Append a line to a file and returns the number of caracters added
    Args:
        filename: The file to append to
        text: The text to append
    Returns:
        The number of caracter added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
