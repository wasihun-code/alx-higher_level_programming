#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    """ Description - Add tuple elements
        Arguments - accepts 2 tuples
        Return - third tuple which is some of first two
    """

    la = len(tuple_a)
    lb = len(tuple_b)

    if la < 2:
        if la == 1:
            a1, a2 = tuple_a[0], 0
        else:
            a1, a2 = 0, 0
    else:
         a1, a2 = tuple_a[0], tuple_a[1]

    if lb < 2:
        if lb == 1:
            b1, b2 = tuple_b[0], 0
        else:
            b1, b2 = 0, 0
    else:
        b1, b2 = tuple_b[0], tuple_b[1]

    sa = a1 + b1
    sb = a2 + b2

    tuple_c = sa, sb

    return tuple_c
