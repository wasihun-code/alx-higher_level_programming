#!/usr/bin/python3
import sys

n = len(sys.argv)

print("Total arguments passed: {}".format(n))

print("Name of script: {}".format(sys.argv[0]))

for i in range(1, n):
    print("{}".format(sys.argv[i]), end=" ")

sum = 0

for i in range(1, n):
    sum +=int(sys.argv[i])

print("\n\nSum of command line arguments: {}".format(sum))
