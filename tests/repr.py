#!/usr/bin/python3


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'__repr__ {self.name}, {self.age}'
    def __str__(self):
        return f'{self.name}, {self.age}'

me = Person("Andrew", 30)
print(me.__repr__())
print(me.__str__())
