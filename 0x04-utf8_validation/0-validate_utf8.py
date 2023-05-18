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
        n //= 2
        # print(digit)
        # toBinary(n // 2)
        toBinary(n)
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
    return (binary)


def validUTF8(data):
    """
    Determines if a given set of data validates UTF-8 encoding
    Valid utf-8 contains 4 byte of data
    if data is of 1 byte - The 8th bit must be 0
    if data is of 2 byte - The leading bit must be 110
    if data is of 3 byte - The leading bit must be 1110
    if data is of 4 byte - The leading bit must br 11110

    Given that integer represents 1 byte of data, therefore
    you only need to handle the 8 least significant bits of each integer
    """
    byte_num = 0
    for num in data:
        # num = bin(num)
        # num = toBinary(num)
        # least_num = int(num[:8])
        # least_num = (num[:8])
        # least_num = int(least_num)
        least_num = num & 255
        if byte_num == 0:
            # if least_num >> 7 == 0:
            if least_num >> 7 == 0:
                # print('Single byte')
                # We have a 1 byte integer
                continue
            # elif least_num >> 5 == 110:
            elif least_num >> 5 == 0b110:
                # print('Two byte')
                byte_num = 1
            # elif least_num >> 4 == 1110:
            elif least_num >> 4 == 0b1110:
                # print('3 byte')
                byte_num = 2
            # elif least_num >> 3 == 11110:
            elif least_num >> 3 == 0b11110:
                # print('4 byte')
                byte_num = 3
            else:
                return False
        else:
            # if least_num >> 6 == 10:
            if least_num >> 6 == 0b10:
                byte_num -= 1
            else:
                return False
    return byte_num == 0
