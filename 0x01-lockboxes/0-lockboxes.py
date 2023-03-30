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
    for box, keys in enumerate(boxes):
        can_unlock = False
        if box > 0 and box not in obj:
            # if box is not already unlocked we want to check if an
            # an already unlocked box has the key to unlock that box
            for key in obj:
                if key < len(boxes) and box in boxes[key]:
                    can_unlock = True
                    break
            if not can_unlock:
                return False
            continue
        keys = boxes[box]
        for key in keys:
            # element = key
            if key < len(boxes):
                # checks if key is a valid box index
                # add the key as the 'key' to the object, obj
                obj[key] = 'unlocked'
            else:
                obj[key] = 'locked'
    return True
