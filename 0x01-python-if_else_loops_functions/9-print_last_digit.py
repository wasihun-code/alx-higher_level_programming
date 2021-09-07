#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        return 0
    last_digit = abs(number) % 10
    return last_digit
