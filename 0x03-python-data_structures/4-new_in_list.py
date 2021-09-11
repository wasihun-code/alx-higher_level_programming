#!/bin/python3

def new_in_list(my_list, idx, element):
    new_list = []
    for i in range(0, len(my_list)):
        if idx < 0:
            new_list = my_list[:]
            break
        elif idx > len(my_list):
            new_list = my_list[:]
            break
        else:
            new_list = my_list[:]
            new_list[idx] = element

        return new_list
