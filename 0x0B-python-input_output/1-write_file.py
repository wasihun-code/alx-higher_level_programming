#!/usr/bin/python3
"""A function that write to a file"""


def write_file(filename="", text=""):
    """This functions writes to a file

    Args:
        filename (str): string to read
        text (str): text to write
    """

    with open(filename, 'w', encoding='utf-8') as a:
        s = a.write(text)
    return s
