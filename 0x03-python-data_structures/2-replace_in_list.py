#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    for i in my_list:
        if (idx < 0):
            return None
            break
        if (idx > len(my_list)):
            return None
            break
    my_list[idx] = element
