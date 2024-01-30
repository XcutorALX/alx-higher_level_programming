#!/usr/bin/python3
"""This module defined a function 'matrix_divided'"""


def matrix_divided(matrix, div):
    """This function divides all entries of a 2 by 2 matrix by div

    Args:
        matrix: a 2 by 2 matrix of integers/floats
        div: a float

    Return: returns the reuslting matrix from the division
    """
    errMsg = "matrix must be a matrix(list of lists) of integers/floats"
    result  = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) != list:
        raise TypeError(errMsg)
    else:
        length = len(matrix[0])
        for row in matrix:
            newRow = []
            if len(row) != length:
                raise TypeError("Each row of the matrix must have the same size")

            if type(row) != list:
                raise TypeError(errMsg)
            else:
                for col in row:
                    if type(col) not in [int, float]:
                        raise TypeError(errMsg)
                    newRow.append(round(col/div, 2))
            result.append(newRow)

    return (result)



