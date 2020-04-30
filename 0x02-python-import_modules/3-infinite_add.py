#!/usr/bin/python3
from sys import argv


def main():
    total = 0
    for i in argv[1:]:
        total += int(i)
    print(total)

if __name__ == "__main__":
    main()
