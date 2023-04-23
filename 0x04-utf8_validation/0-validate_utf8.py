#!/usr/bin/python3
"""
Validates a character to UTF-8
"""

# l = []
'''
def toBinary(n):
    l = ''
    digit = 0
    if n > 1:
        # n = n // 2
        # print(digit)
        toBinary(n // 2)
    # digit = n % 2
    # print(n % 2, end='')
    s = n % 2
    return s
'''


def toBinary(n):
    """
    Convert a positive integer n to base 2
    """
    binary = ''
    if n == 0:
        return '0'
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary


def validUTF8(data):
    """
    Validates if the character in data are vakid for utf-8
    """
    for num in data:
        binary = toBinary(num)
        # print(num, binary)
        # print(len(binary))
        if len(binary) > 8:
            # print('Here')
            return False
    return True
