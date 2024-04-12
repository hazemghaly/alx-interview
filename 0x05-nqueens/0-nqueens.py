#!/usr/bin/python3

import sys

def queens(N):
    """Nqueens"""
    result = []
    N = int(sys.argv[1])
    board = [[0] * N for _ in range(N)]
    stack = []  # Stack to simulate recursive calls
    row, col = 0, 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not isinstance(N, int):
        print("N must be a number")
        exit(1)
    elif N < 4:
        print("N must be at least 4")
        exit(1)

    if (col >= 4):
        v = []
        for i in board:
          for j in range(len(i)):
            if i[j] == 1:
              v.append(j+1)
        result.append(v)
        return True
    res = False
    for i in range(4):
        if (board, i, col, N):
            board[i][col] = 1
            res = queens(N) or res
            board[i][col] = 0  # BACKTRACK
    return res


if __name__ == "__main__":
    queens(4)
