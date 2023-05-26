#!/usr/bin/python3
"""
Nqueens using backtracking
"""
import sys
from random import randint


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)


def nqueens(n):
    """
    Places N non-attacking queens on an n * n chessboard
    """
    posDiag = []
    negDiag = []
    queen = []
    res = []

    board = []
    for i in range(n):
        square = [0 for i in range(n)]
        board.append(square)

    solutions = backtrack(0, board, posDiag, negDiag, queen, res)
    return print_solution(solutions)


def print_solution(solutions):
    """
    Prints the postion of the non-attacking queens from the chess board
    """

    for solution in solutions:
        s = []
        for i, row in enumerate(solution):
            for j, col in enumerate(row):
                if col == 1:
                    s.append([i, j])
        print(s)


def backtrack(row, board, posDiag, negDiag, queen, res):
    """
    Using the backtracking algorithm finds the right position of a queen
    where it will not attack another queen
    """

    if row == n:
        # copy = [row for row in board]
        copy = [row[:] for row in board]
        res.append(copy)
        return
    for col in range(n):
        if col in queen or (row + col) in posDiag or (row - col) in negDiag:
            continue
        queen.append(col)
        posDiag.append(row + col)
        negDiag.append(row - col)
        board[row][col] = 1

        backtrack(row + 1, board, posDiag, negDiag, queen, res)

        queen.remove(col)
        posDiag.remove(row + col)
        negDiag.remove(row - col)
        board[row][col] = 0

    return res


if __name__ == "__main__":
    nqueens(n)
