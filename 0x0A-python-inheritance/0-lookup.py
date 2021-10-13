#!/usr/bin/python3
"""Documentation for lookup module."""


def lookup(obj):
    """Returns a list object of available attributes and methods."""

    return list(dir(obj))
