#!/usr/bin/python3


class P:
    a = "class attribute" # accessed by all the Instances of the class

x = P()
print(">>> {} == x.a".format(x.a))

l = P()
print(">>> {} == l.a".format(l.a))

print("Also the class can use that")
print(">>> {} == P.a".format(P.a))

print("Now changing an instance class attribute")
x.a = "Now I am instance changed class attribute."
print(">>> {} == x.a but changed".format(x.a))

print("Now changing the attribute in the class NOT INSTANCE ATTRIBUTE")
P.a = "chnaged class"
print(">>> {} == P.a but changed".format(P.a))

x = P()
print(">>> {} == x.a".format(x.a))

l = P()
print(">>> {} == l.a".format(l.a))
