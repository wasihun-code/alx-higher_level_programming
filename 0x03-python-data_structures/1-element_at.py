#!/usr/bin/python3


def element_at(my_list, idx):
    for i in my_list:
        if (idx < 0):
            return None
            break
        if (idx > len(my_list)):
            return None
            break
        return my_list[idx]
