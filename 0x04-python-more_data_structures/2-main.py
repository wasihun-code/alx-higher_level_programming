#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

my_list = [1, 3, 1, 4, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

my_list = [0]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

my_list = [1, 1, 1, 1]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

my_list = []
result = uniq_add(my_list)
print("Result: {:d}".format(result))
