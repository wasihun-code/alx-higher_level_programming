#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    new_list = []

    for i in range(len(my_list)):
        new_list.append(my_list[-i])

    for i in range(len(new_list)):
        print("{}".format(new_list[i]))
