#!/bin/python3

def new_in_list(my_list, idx, element):

    new_list = []
    l = len(my_list)

    for i in range(l):
        if idx < 0 or idx > l:
            new_list = my_list[:]
        else:
            new_list = my_list[:]
            new_list[idx] = element

        return new_list
