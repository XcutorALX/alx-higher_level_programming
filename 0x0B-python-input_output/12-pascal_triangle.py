#!/usr/bin/python3
"""This module contains a pascal_triangle func"""


def pascal_triangle(n):
    """This function returns a list representing a
    pascal triangle of n rows
    """

    triangle = []

    if n < 0:
        return triangle

    for i in range(n):
        row = []

        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        triangle.append(row)

    return triangle
