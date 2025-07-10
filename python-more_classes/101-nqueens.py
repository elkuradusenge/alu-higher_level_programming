#!/usr/bin/python3
"""
N-Queens problem solver.

This script prints all possible solutions to the N-Queens puzzle.
Usage:
    ./nqueens.py N
where N is the size of the chessboard (and number of queens),
and must be an integer greater than or equal to 4.
"""

import sys


def is_valid(board, row, col):
    """
    Check if a queen can be placed at (row, col).

    Args:
        board (list of tuples): Positions of queens placed so far as (row, col).
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        bool: True if placing the queen is valid, False otherwise.
    """
    for r, c in board:
        if c == col or r + c == row + col or r - c == row - col:
            return False
    return True


def nqueens_helper(n, row, board, solutions):
    """
    Recursive helper to find all solutions for N-Queens.

    Args:
        n (int): Size of the chessboard.
        row (int): Current row to place a queen.
        board (list): Positions of queens placed so far.
        solutions (list): List to collect all valid solutions.
    """
    if row == n:
        solutions.append(board.copy())
    else:
        for col in range(n):
            if is_valid(board, row, col):
                board.append((row, col))
                nqueens_helper(n, row + 1, board, solutions)
                board.pop()


def nqueens(n):
    """
    Solve the N-Queens problem and print all solutions.

    Args:
        n (int): The size of the board and number of queens.
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    nqueens_helper(n, 0, [], solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
