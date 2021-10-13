#!/usr/bin/python3
"""Documentation for module is_same_class."""


def is_same_class(obj, a_class):
    """Returns true if obj is instance of a_class """

    if isinstance(obj, a_class):
        return True
    else:
        return False
