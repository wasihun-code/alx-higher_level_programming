#!/usr/bin/python3


def multiple_returns(sentence):

    length = len(sentence)
    first = None

    if length > 0:
        first = sentence[0]

    ts = (length, first)

    return ts
