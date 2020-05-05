#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not any(matrix):
        print()
    for x in matrix:
        for idx, y in enumerate(x):
            print("{:d}".format(y), end='\n' if idx is len(x) - 1 else ' ')
