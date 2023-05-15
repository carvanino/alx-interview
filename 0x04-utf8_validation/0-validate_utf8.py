#!/usr/bin/python3
"""
UTF-8 Validation
"""


def toBinary(n):
    """
    Converts an integer to binary
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
    Determines if a given set of data validates UTF-8 encoding
    Valid utf-8 contains 4 byte of data
    if data is of 1 byte - The 8th bit must be 0
    if data is of 2 byte - The leadinjlg bit must be 110
    if data is of 3 byte - The leading bit must be 1110
    if data is of 4 byte - The leading bit must br 11110

    Given that integer represents 1 byte of data, therefore
    you only need to handle the 8 least significant bits of each integer
    """
    byte_num = 0
    for num in data:
        # num = bin(num)
        # least_num = int(num[:8])
        # print(least_num)
        if byte_num == 0:
            # if least_num >> 111 == 0:
            if num >> 7 == 0:
                # print('Single byte')
                # We have a 1 byte integer
                continue
            # elif least_num >> 101 == 110:
            elif num >> 5 == 0b110:
                # print('Two byte')
                byte_num = 1
            # elif least_num >> 100 == 1110:
            elif num & 4 == 0b1110:
                # print('3 byte')
                byte_num = 2
            # elif least_num >> 11 == 11110:
            elif num & 3 == 0b11110:
                # print('4 byte')
                byte_num = 3
            else:
                # print('Not here na')
                return False
        else:
            # if least_num >> 110 == 10:
            if num & 6 == 0b10:
                byte_num -= 1
            else:
                return False
    return byte_num == 0

# print(validUTF8([229, 65, 127, 256]))
