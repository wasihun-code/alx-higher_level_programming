#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    n = len(sys.argv)
    total = 0

    for i in range(n-1):
        total += int(sys.argv[i + 1])

    print(total)
