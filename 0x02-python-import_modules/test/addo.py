#!/usr/bin/python3
def add(a, b):
    print("{}".format(a + b))

if __name__ == "__main__":
    import sys
    add(int(sys.argv[1]), int(sys.argv[2]))
