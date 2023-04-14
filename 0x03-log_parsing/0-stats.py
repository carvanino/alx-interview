#!/usr/bin/python3
"""
Task 0 - Log parsing
"""

import sys


def parse_log():
    count = 0
    fileSize = 0
    pStatusCode = [200, 301, 400, 401, 403, 404, 405, 500]
    statusCodeOccurence = {}

    try:
        for line in sys.stdin:
            try:
                each = line.split()
                count += 1
                fileSize += int(each[-1:][0])
                statusCode = int(each[-2:][0])
                if statusCode in pStatusCode:
                    if statusCode in statusCodeOccurence:
                        statusCodeOccurence[statusCode] += 1
                    else:
                        statusCodeOccurence[statusCode] = 1

                if count == 10:
                    count = 0
                    raise ValueError("Count Reached 10")
            except ValueError as err:
                print_error(fileSize, statusCodeOccurence, err)
                continue
    except KeyboardInterrupt:
        print_error(fileSize, statusCodeOccurence, "KeyboardInterrupt")


def print_error(fileSize, statusCodeOccurence, error):
    print('File size: {}'.format(fileSize))
    for items in sorted(statusCodeOccurence.items()):
        print('{}: {}'.format(items[0], items[1]))


if __name__ == '__main__':
    parse_log()
