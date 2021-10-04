#!/usr/bin/python3
"""
this is the "example" module.

>>> add(2, 3)
5
"""

def add(a, b):
    """Return the sum of a and b.

    >>> add(2, 3)
    5
    >>> add(0, 2)
    Traceback (most recent call last):
        ...
    ValueError: a must be > 0

    >>> add(3, 0)
    Traceback (most recent call last):
        ...
    ValueError: b must be > 0
    """

    if a <= 0:
        raise ValueError("a must be > 0")
    if b <= 0:
        raise ValueError("b must be > 0")
    return (a + b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
