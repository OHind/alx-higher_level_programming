#!/usr/bin/python3
"""Writing a function"""


def write_file(filename="", text=""):
    """ Write a file
    Args:
        filename: the file to write in
        text: The text to write
    Returns:
        the number of caracter written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
