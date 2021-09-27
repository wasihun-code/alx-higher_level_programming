#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):

    printed_numbers = 0
    for i in range(0, x):
        try:
            i = int(i)
            print("{:d}".format(my_list[i]), end='')
            printed_numbers += 1
        except (ValueError, TypeError):
            pass
    print()

    return printed_numbers
