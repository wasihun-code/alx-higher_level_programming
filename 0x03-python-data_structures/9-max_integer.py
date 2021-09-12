#!/usr/bin/python3


def max_integer(my_list=[]):
    maximum = 0
    l = len(my_list)

    if l == 0:
        return None

    maximum = my_list[0]

    for i in range(0, l):
        if my_list[i] > maximum:
            maximum = my_list[i]

    return maximum
