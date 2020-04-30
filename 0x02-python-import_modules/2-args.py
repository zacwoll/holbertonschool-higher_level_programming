#!/usr/bin/python3
from sys import argv


def main():
    argc = len(argv)
    if argc > 1:
        print("{} argument".format(argc - 1), end='')
        if argc > 2:
            print("s", end='')
        print(":")
        for i, val in enumerate(argv[1:], 1):
            print("{}: {}".format(i, val))
    else:
        print("0 arguments.")
if __name__ == "__main__":
    main()
