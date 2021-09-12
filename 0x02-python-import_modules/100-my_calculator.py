#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    if (len(sys.argv) - 1 != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    num1, operator, num2 = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    op = {"+": add, "-": sub, "*": mul, "/": div}

    if sys.argv[2] not in list(op.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}"
        .format(num1, sys.argv[2], num2, op[sys.argv[2]](num1, num2)))
