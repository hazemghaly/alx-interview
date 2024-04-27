#!/usr/bin/python3
"""interview """


import sys


def is_available(board, row, col, N):
    """check availablty of this board"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve(board, col, N, result):
    """Solve Nqueens with recursive """
    if col >= N:
        v = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    v.append([i, j])
        result.append(v)
        return True

    res = False
    for i in range(N):
        if is_available(board, i, col, N):
            board[i][col] = 1
            res = solve(board, col + 1, N, result) or res
            board[i][col] = 0  # Backtrack

    return res


def queens(N):
    """check cmd arguments"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)
    board = [[0] * N for _ in range(N)]
    result = []
    if not solve(board, 0, N, result):
        print("Solution does not exist")
        return
    for res in result:
        print(res)


if __name__ == "__main__":
    queens(4)
