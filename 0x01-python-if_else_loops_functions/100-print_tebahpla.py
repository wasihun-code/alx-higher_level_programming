#!/usr/bin/python3
for num in range(122, 96, -1):
	if num % 2 == 1:
		ascii_num = num - 32
	print("{:c}".format(num), end='')
