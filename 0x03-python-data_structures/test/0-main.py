#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
print("--")
my_list = [1, 2, ]
print_list_integer(my_list)
print("--")
my_list = [1, 232, 3, 44, 5]
print_list_integer(my_list)
print("--")
my_list = [1, 2, 3, 4, 5, 89, 29, 29]
print_list_integer(my_list)
print("--")
my_list = []
print_list_integer(my_list)
