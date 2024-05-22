#!/usr/bin/python3
'''interview taskes
'''


def canUnlockAll(boxes):
    """ Method that determines if all boxes can be opened """
    for key in range(1, len(boxes)):
        res = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                res = True
                break
        if not res:
            return False
    return True
