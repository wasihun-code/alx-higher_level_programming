#!/usr/bin/python3
import sys
l = len(sys.argv)


def printArguments():
    """Print command line arguments

    Args:
        command line arguments

    Return:
        0 since void
    """

    if (l == 2):
        print("{} argument:".format(l - 1))
        print("{}: {}".format(1, sys.argv[1]))

    else:
        print("{} arguments:".format(l - 1))
        for i in range(1, l):
            print("{}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    printArguments()
