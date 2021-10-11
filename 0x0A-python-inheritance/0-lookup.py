#!/usr/bin/python3

def lookup(obj):
    """Returns a list object of available attributes and methods."""

    return list(dir(obj))
