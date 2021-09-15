#!/usr/bin/python3


def multiply_by_2(a_dictionary):

    new = dict(a_dictionary)

    for a, b in new.items():
        new[a] = 2 * new[a]

    return new
