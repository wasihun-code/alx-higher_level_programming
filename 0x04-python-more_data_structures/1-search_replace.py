#!/usr/bin/python3


def search_replace(my_list, search, replace):

    if my_list is None:
        return None

    new = my_list.copy()

    for i in new:
        if i == search:
            new[new.index(i)] = replace
        else:
            continue
    return new
