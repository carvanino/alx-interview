#!/usr/bin/python3
"""
Implement lockboxes
"""


def canUnlockAll(boxes):

    """
    Takes a list of lists as an argument and where each box contains the key
    to the any other box, the first box is unloack by default
    """

    obj = {}
    for box in range(len(boxes)):
        # print(obj)
        # print('Box ', box)
        if box > 0 and box not in obj.keys():
            for key, value in obj.items():
                # if key == box and value == 'unlocked':
                if box in boxes[key]:
                    return True
            return False
        keys = boxes[box]
        for key in range(len(keys)):
            if keys[key] < len(boxes):
                element = keys[key]
                obj[element] = 'unlocked'
            else:
                obj[element] = 'locked'
    return True
