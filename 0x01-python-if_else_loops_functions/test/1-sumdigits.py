#!/usr/bin/python3
def sumDigits(n):
	sum = 0
	while (n > 0):
		sum = sum + int(n%10)
		n = int(n / 10)
	print(sum)
f = sumDigits
f(100)


