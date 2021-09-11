#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    num1, op, num2 = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])

    if op == '+':
        res = add(num1, num2)
    elif op == '-':
        res = sub(num1, num2)
    elif op == '/':
        res = div(num1, num2)
    elif op == '*':
        res = mul(num1, num2)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{:d} {:d} {} = {:d}".format(num1, op, num2, res))
