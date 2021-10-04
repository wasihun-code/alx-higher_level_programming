#!/usr/bin/python3

class C:

    counter = 0

    def __init__(self):
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1

if __name__ == "__main__":
    a = C()
    print("No of instances >>> " + str(C.counter))
    b = C()
    print("No of instances >>> " + str(C.counter))
    c = C()
    print("No of instances >>> " + str(C.counter))
    d = C()
    print("No of instances >>> " + str(C.counter))
    e = C()
    print("No of instances >>> " + str(C.counter))
