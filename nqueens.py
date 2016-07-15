#!/usr/bin/env python
import sys
import collections
from copy import deepcopy


def print_board(board):
    ret = ''
    for row in board:
        for square in row:
            ret += 'Q' if square else '.'
        ret += '\n'
    print(ret)


def is_valid(board):
    """
    This is the especially clever part. Each row, column, down-right diagonal,
    and up-right diagonal are associated with and ID (eg. row8, dU2, etc.).
    A double-for-loop iterates through each of the squares on the board. If
    more than one queen exist on any row, column, or diagonal, then the board
    is not valid, otherwise it is.
    """
    counts = collections.Counter()
    n = len(board)
    for row in range(n):
        for col in range(n):
            if board[row][col]:
                counts['row' + str(row)] += 1 
                counts['col' + str(col)] += 1
                counts['dU' + str(col + row)] += 1
                counts['dD' + str(col + ((n-1) - row))] += 1 
    for value in counts.values():
        if value > 1:
            return False
    return True


def next(board, row):
    if row == len(board):
        print_board(board)
        return
    else:
        for col in range(len(board)):
            copy = deepcopy(board)
            copy[row][col] = 1
            if is_valid(copy):
                next(copy, row + 1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Please pass in the size of the board.")
    n = int(sys.argv[1])
    board = [[0 for i in range(n)] for i in range(n)]
    next(board, 0)

