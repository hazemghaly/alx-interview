#!/usr/bin/python3
'''interview taskes
'''


def pascal_triangle(n):
    '''interview taske pascal triangle'''
    if n <= 0:
        return []
    res = [[1]]
    if n == 1:
        return res
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(res[i - 1][j - 1] + res[i - 1][j])
        row.append(1)
        res.append(row)
    return res
