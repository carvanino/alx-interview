#!/usr/bin/python3


"""
A list of lists of integers representing the pascals triangle
"""


def pascal_triangle(n):
    """
    Takes n as the height of the triangle and implement
    a pascals triangle
    """
    array = []
    triangle = []
    if n <= 0:
        return array
    for row in range(n):
        # print('ROW', row)
        if row == 0:
            array.append(1)
        arry = [1 for i in range(row + 1)]
        for col in range(row):
            if col > 0:
                new = array[col - 1] + array[col]
                arry[col] = new
        array = arry.copy()
        triangle.append(array)
        # print(array)
    return triangle
