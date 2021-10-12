#!/usr/bin/python3
"""A function that reads from a file and prints its output."""


def read_file(filename=""):
    """This functions reads from a file

    Args:
        filename (str): string to read
    """

    with open(filename, 'r',encoding='utf-8') as a:
        for l in a:
            print(l, end='')
