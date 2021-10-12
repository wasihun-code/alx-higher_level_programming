#!/usr/bin/python3
"""A function that write to a file"""


def append_write(filename="", text=""):
    """This functions writes to a file

    Args:
        filename (str): string to read
        text (str): text to write
    """

    with open(filename, 'a', encoding='utf-8') as a:
        s = a.write(text)

    return s
