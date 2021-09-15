#!/usr/bin/python3


def best_score(a_dictionary):

    if a_dictionary is None:
        return None

    key = list(a_dictionary.keys())
    val = list(a_dictionary.values())
    maximum = 0

    for i, v in a_dictionary.items():
        if v > maximum:
            maximum = v

    pos = val.index(maximum)

    return key[pos]
