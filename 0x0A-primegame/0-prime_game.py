#!/usr/bin/python3
"""
Implements a function isWinner that determines the winner for a Prime game
of two players
"""


def isWinner(x, nums):
    """
    The isWinner function
    """
    rounds = 0
    while rounds != x:
        Marie = 0
        Ben = 0
        for num in nums:
            numbers = list(range(1, num + 1))
            primes = get_primes(2, num)

            if len(primes) < 1:
                turn = 'Ben'
            else:
                turn = 'Marie'

            count = 1
            for prime in primes:
                for n in numbers[:]:
                    if n % prime == 0:
                        numbers.remove(n)

                if count % 2 == 0:
                    turn = 'Ben'
                else:
                    turn = 'Marie'

                count += 1

            if len(numbers) <= 1 and turn == 'Marie':
                Marie += 1
            else:
                Ben += 1

        rounds += 1

        if Marie > Ben:
            return 'Maria'
        elif Ben < Marie:
            return 'Ben'
        else:
            return 'None'


def get_primes(start, end):
    """
    Returns a list of prime numbers in the range from 'start'
    to 'end' (inclusive).
    """
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def is_prime(num):
    """
    Checks if a number is prime.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
