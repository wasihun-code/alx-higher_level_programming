#!/usr/bin/python3
import sys
total = 0
n = len(sys.argv)

def infinite_add():
    if (n == 1):
        print("0")
    else:
        for i in range(1, n):
            total += int(sys.argv[i])
        print("{}".format(total))

if __name__ == "__main":
    infinite_add()
