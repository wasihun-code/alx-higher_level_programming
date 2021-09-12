#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    size = len(my_list)

    if size > 0:
        for i in range(size):
            if idx < 0 or idx > size:
                continue
            else:
                my_list[idx] = element
    return my_list
