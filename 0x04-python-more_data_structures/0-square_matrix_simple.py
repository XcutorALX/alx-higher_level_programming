#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return []
    if len(matrix) != len(matrix[0]) or len(matrix) != len(matrix[1]):
        return []

    result = []

    for row in matrix:
        rowResult = []
        for col in row:
            rowResult.append(col ** 2)

        result.append(rowResult)

    return result
