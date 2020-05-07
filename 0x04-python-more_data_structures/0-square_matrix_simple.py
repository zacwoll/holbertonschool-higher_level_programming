#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for x in matrix:
        new_mat.append(list(map(lambda x: x**2, x)))
    return new_mat
