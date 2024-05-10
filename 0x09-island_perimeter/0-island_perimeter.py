#!/usr/bin/python3
'''interview taskes
'''


def island_perimeter(grid):
    ''' island prrimeter task interview
'''
    if grid == [] or len(grid) == 0:
        return 0
    i, r, c = 0, 0, 0
    a = len(grid)
    b = len(grid[0])
    for r in range(0, a):
        for c in range(0, b):
            if grid[r][c] != 0:
                i += 4
                if (r < a - 1 and grid[r + 1][c] == 1):
                    i -= 2
                if (c < b - 1 and grid[r][c + 1] == 1):
                    i -= 2
            c += 1
        r += 1
        c = 0
    return i
