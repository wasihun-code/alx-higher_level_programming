#!/usr/bin/python3

def no_c(my_string):

    no_cs = ""

    for i in my_string:
        if i == 'C' or i == 'c':
            continue
        else:
            no_cs = no_cs + i

    return no_cs
