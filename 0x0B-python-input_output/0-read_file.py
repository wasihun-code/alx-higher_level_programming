#!/usr/bin/python3


def read_file(filename=""):
    """This functions reads from a file."""

    with open(filename, 'r',encoding='utf-8') as a:
        for l in a:
            print(l)
