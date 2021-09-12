#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

my_list = []
print_reversed_list_integer(my_list)

my_list=[23, 56, 78, 52, 322]
print_reversed_list_integer(my_list)

my_list=[23, 56, 78, 52]
print_reversed_list_integer(my_list)

my_list=[-23, 56, 78, 52, -322]
print_reversed_list_integer(my_list)

my_list=[23, 56, 78]
print_reversed_list_integer(my_list)
