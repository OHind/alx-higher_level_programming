#!/usr/bin/python3
""" Reading a file"""


def read_file(filename=""):
    """A function that reads a file
    Args:
        filename: the file to read
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
