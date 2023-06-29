#!/usr/bin/python3
"""
Implements a function isWinner that determines the winner for a Prime game
of two players
"""


def isWinner(x, nums):
    """
    player_1 and player_2 selects the first prime number from the
    range of a list of numbers and remove the multiples of the selected
    prime number from the list of orginal number. A player that is left
    without any number to remove from the list loses the game

    Args:
        x (int) : The number of rounds they have to go to determine a winner
        nums (list): A list of number for each round.
    Return:
        The name of the winner
    """
    rounds = 1
    while rounds != x:
        Marie = 0
        Ben = 0
        for num in nums:
            # print('ROUNDS = ', rounds)
            # num = 4
            numbers = []
            for n in range(1, num + 1):
                numbers.append(n)
            # numbers = [1, 2, 3, 4]

            primes = get_primes(1, num)
            # print(primes)
            # primes = [2, 3]
            if len(primes) < 1:
                turn = 'Ben'

            count = 1
            for prime in primes:
                # print('prime', prime)
                # prime = 2
                # print('COUNT = ', count)
                for n in numbers[:]:
                    # print('>>>>>>>>>> ', len(numbers))
                    # print(n)
                    if n % prime == 0:
                        # print('{} is a multiple of {}'.format(n, prime))
                        numbers.remove(n)
                    # Bens turn to play
                if count % 2 == 0:
                    # Ben += 1
                    turn = 'Ben'
                    # print('Bens Turn')
                    # print('prime is ', prime)
                    # print('number is ', numbers)
                else:
                    # Marie += 1
                    turn = 'Marie'
                    # print('Marie turn')
                    # print('prime is ', prime)
                    # print('number is ', numbers)

                count += 1

            if len(numbers) <= 1 and turn == 'Marie':
                # print('{} wins this round'.format(turn))
                Marie += 1
            else:
                # print('{} wins this round'.format(turn))
                Ben += 1

                # count += 1

            rounds += 1

        # print('MAries score is ', Marie)
        # print('Ben score is ', Ben)

        if Marie > Ben:
            return 'Marie'
        elif Marie == Ben:
            return 'None'
        else:
            return 'Ben'


'''
def get_multiples(prime, num):
    multiples = []
    for n in range(prime, num + 1):
        if n % prime == 0:
            multiples.append(n)

    return multiples
'''


def get_primes(start, end):
    """
    """
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def is_prime(num):
    """
    """
    if num <= 1:
        return False
    for i in range(2, (int(num ** 0.5) + 1)):
        if num % i == 0:
            return False
    return True

# print(get_primes(1, 9))
