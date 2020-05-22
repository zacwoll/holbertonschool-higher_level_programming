#!/usr/bin/python3
"""
This module containts matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix, divided by div
    """
    matrix_err = 'matrix must be a matrix (list of lists) of integers/floats'

    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError(matrix_err)

    for y in matrix:
        if type(y) is not list or len(y) is 0:
            raise TypeError(matrix_err)
        if len(y) is not len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        if not all(type(x) is int or type(x) is float for x in y):
            raise TypeError(matrix_err)
    if div is 0:
        raise ZeroDivisionError('division by zero')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')

    new_mat = []
    for y in matrix:
        new_row = [round(x / div, 2) for x in y]
        new_mat.append(new_row)
    return new_mat
