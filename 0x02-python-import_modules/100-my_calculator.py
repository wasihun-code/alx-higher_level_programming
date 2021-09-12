#!/usr/bin/python3

if __name__ == "__main__":

    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(op.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    num1, num2, c = int(sys.argv[1]), int(sys.argv[3]), sys.argv[2]

    print("{} {} {} = {}".format(num1, c, num2, op[c](num1, num2)))
