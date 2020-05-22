#!/usr/bin/python3
"""
This matrix-mul module contains only mtrix_mul
"""


def matrix_mul(m_a, m_b):
    """
    returns the product of two matrices
    """
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')

    for y in m_a:
        if type(y) is not list:
            raise TypeError('m_a must be a list of lists')
    for y in m_b:
        if type(y) is not list:
            raise TypeError('m_b must be a list of lists')

    if len(m_a) is 0:
        raise ValueError('m_a can\'t be empty')
    if len(m_b) is 0:
        raise ValueError('m_b can\'t be empty')

    for y in m_a:
        if len(y) is 0:
            raise ValueError('m_a can\'t be empty')
    for y in m_b:
        if len(y) is 0:
            raise ValueError('m_b can\'t be empty')

    for y in m_a:
        if not all(type(x) is int or type(x) is float for x in y):
            raise TypeError('m_a should contain only integers or floats')
    for y in m_b:
        if not all(type(x) is int or type(x) is float for x in y):
            raise TypeError('m_b should contain only integers or floats')

    for y in m_a:
        if len(y) is not len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
    for y in m_b:
        if len(y) is not len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) is not len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    new_mat = [[sum(a*b for a, b in zip(x, y)) for y in zip(*m_b)]
               for x in m_a]
    return (new_mat)
