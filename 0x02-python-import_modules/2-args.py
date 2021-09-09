#!/usr/bin/python3
import sys
l = len(sys.argv)
if (l == 1):
    print("0 arguments.")
elif (l == 2):
    print("1 argument.")
    print("{}: {}".format(1, sys.argv[1]))
else:
    print("{} arguments.".format(l - 1))
    for i in range(1, l):
        print("{}: {}".format(i, sys.argv[i]))
