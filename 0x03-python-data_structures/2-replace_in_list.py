#!/usr/bin/python3


def replace_in_list(my_list, idx, element):

    l = len(my_list)

    for i in range(l):
        if l <= 0 or idx < 0 or idx > l - 1:
            continue
        else:
            my_list[idx] = element

    return my_list
