#!/usr/bin/python3
"""
Task 0 - Change comes from within
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet total
    """
    coins = sorted(coins)
    if total <= 0:
        return 0
    maxi = max(coins)
    hmax = 0
    count = 0
    while (hmax + maxi < total):
        hmax += maxi
        count += 1

    target = total - hmax
    coins.remove(maxi)
    finder = 0
    maxi = max(coins)
    # count = 1
    while (finder != target):
        if (finder < target):
            finder += maxi
            count += 1
        if finder > target:
            finder -= maxi
            count -= 1
            coins.remove(maxi)
            if (len(coins) <= 0):
                return -1
            maxi = max(coins)
        if finder == target:
            # coins.remove(maxi)
            return count

    '''
    print('Finder is ', finder)
    print('Count is ', count)
    print('Current sum is', sum(coins))



if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))

    print(makeChange([1, 5, 10, 25], 43))

    print(makeChange([1, 7, 13, 21], 50))

    print(makeChange([1, 3, 5, 9], 15))

    print(makeChange([1, 4, 6, 8], 12))

    print(makeChange([1, 2, 5, 10, 20], 37))

    print(makeChange([1, 3, 4, 7], 10))
'''
