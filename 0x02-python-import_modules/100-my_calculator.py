#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operation = {
            '+': add,
            '-': sub,
            '/': div,
            '*': mul
        }
        if argv[2] in '+-/*':
            ans = operation[argv[2]](int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], ans))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
