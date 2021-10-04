#!/usr/bin/python3
"""Returns the addition of two integers or floats"""


def add_integer(a, b=98):
    """Returns the sum of two integers.

    Args:
        a (int): First number
        b (int): Second number
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
