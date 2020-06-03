#!/usr/bin/python3
""" 14-pascal_triangle """


def pascal_triangle(n):
    """ return list of lists representing pascal's triangle at n """
    tri = []
    res = [[1]]
    if n <= 0:
        return tri
    if n == 1:
        return res
    while (n - 1):
        new_tri = [1]
        for i in range(len(tri) - 1):
            new_tri.append(tri[i] + tri[i + 1])
        new_tri.append(1)
        n -= 1
        res.append(new_tri)
        tri = new_tri
    return res
