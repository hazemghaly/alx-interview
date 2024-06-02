#!/usr/bin/python3
"""
“Minimum Operations” problem effectively
"""


def minOperations(n):
    """ Minimum Operations needed to get n H characters """
    m = 2
    t = 0
    while n > 1:
        while n % m == 0:
            t += m
            n /= m
        m += 1
    return t
