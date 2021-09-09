#!/usr/bin/python3
import sys
n = len(sys.argv)

def infinite_add():
        total = 0
        for i in range(1, n):
            total += int(sys.argv[i])
        print(total)
if __name__ == "__main":
    infinite_add()
