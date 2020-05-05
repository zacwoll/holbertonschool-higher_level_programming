#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
#    if not any(matrix):
#        print()
    for x in matrix:
        for idx, y in enumerate(x):
            print("{:d}".format(y), end='\n' if idx is len(x) - 1 else ' ')

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
