#!/usr/bin/python3
"""
Rotates a 2D Matrix, clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix by 90 degrees clockwise in-place
    """
    n = len(matrix)
    rows = n  # 3
    cols = len(matrix[0])  # 3
    # print("row = ", rows)
    # print("col = ", cols)
    transpose_matrix(matrix, cols)
    reverse_rows(matrix, rows)
    # print(matrix)


def transpose_matrix(matrix, cols):
    """
    Transposes a matrix
    """
    for i in (range(cols - 1, -1, -1)):
        for j in (range(i)):
            matrix[i][j],  matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_rows(matrix, rows):
    """
    Reverses the rows in a matrix
    """
    for i in range(rows):
        start = 0
        end = rows - 1
        while (start < end):
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start += 1
            end -= 1


'''
def rotate_2d_matrix(matrix):
    """
    Transposes a 2D - matrix and reverses the rows
    i.e. Rotates a matrix, returns the rotated matrix
    """
    n = len(matrix)
    # m = len(matrix[0])
    count = n * n
    index = 0
    T_matrix = []
    while count > 0:
        T_rows = []
        for row in range(n-1, -1, -1):
            T_rows.append(matrix[row][index])
            count -= 1
        T_matrix.append(T_rows)
        index += 1
    print(T_matrix)
    return T_matrix
'''
