#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """prints reverse of a given 
       list like c.
    """

    new_list = []
    my_list.reverse()

    for i in my_list:
        new_list.append(i)

    for i in new_list:
        print("{}".format(i))

    
