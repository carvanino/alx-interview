#!/usr/bin/python3
"""
Implements a method that calculates the number of operation
needed to result in n of H characters in the a file, given that
The text file only contains a single character H and the text editor
can only complete two operations in the file: Copy All and Paste
"""


def isPrime(n):
    """
    Checks if n is a prime number
    """

    for i in range(2, (n // 2)):
        if n % i == 0:
            return False
    return True


def prime_factors(n):
    """
    Returns all the prime factors of the number n
    """
    factors = []
    for i in range(2, (n//2)+1):
        #for i in range(2, int(n**0.5+1)):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 1:
        factors.append(n)
    return factors


def minOperations(n):
    """
    Returns an Integer which indicates the fewest number of opertions to get
    the n of H character in the file given the minimal type of operations
    allowable
    """
    if n <= 1:
        return 0
    sum = 0
    for i in prime_factors(n):
        sum += i
    return sum
