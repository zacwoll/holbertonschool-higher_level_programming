#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def main():
if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
ops = ['+', '-', '*', '/']
op_list = [lambda a, b:add(a, b), lambda a, b:sub(a, b), lambda a, b:mul(a, b),
           lambda a, b:div(a, b)]
if argv[2] in ops:
    a = int(argv[1])
    b = int(argv[2])
    result = op_list[ops.index(argv[2])](a, b)
    print(result)
else:
    print("Unknown operator. Available ops: +, -, * and /")
    exit(1)

if __name__ == "__main__":
    main()
