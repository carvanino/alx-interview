#!/usr/bin/python3
"""
Task 0 - Log parsing
"""

from sys import stdin

count = 0
fileSize = 0
pStatusCode = [200, 301, 400, 401, 403, 404, 405, 500]
statusCodeOccurence = {}

try:
    for line in stdin:
        try:
            each = line.split()
            count = count + 1
            # print(each[-1:][0])
            # fileSize += int(each[len(each)-1])
            fileSize += int(each[-1:][0])
            statusCode = int(each[-2:][0])
            codeCount = 0
            if statusCode in pStatusCode:
                if statusCode in statusCodeOccurence:
                    statusCodeOccurence[statusCode] += 1
                else:
                    statusCodeOccurence[statusCode] = 1

            # print("line {} -> {}".format(count, each))

            if count == 10:
                count = 0
                raise ValueError("Count Reached 10")
                '''
                print('File size: {}'.format(fileSize))
                # print(statusCodeOccurence)
                for items in sorted(statusCodeOccurence.items()):
                    print('{}: {}'.format(items[0], items[1]))
                    # print(list(items))
                statusCodeOccurence.clear()
                '''
                # print
                # raise ValueError("Count Reached 10")
        except ValueError as err:
            print('File size: {}'.format(fileSize))
            for items in sorted(statusCodeOccurence.items()):
                print('{}: {}'.format(items[0], items[1]))
            statusCodeOccurence.clear()
            # print("Exception occurred:", err)
            # print(count)
            continue
except KeyboardInterrupt:
    print('File size: {}'.format(fileSize))
    for items in sorted(statusCodeOccurence.items()):
        print('{}: {}'.format(items[0], items[1]))
    statusCodeOccurence.clear()
    # print("KeyboardInterrupt occurred")
