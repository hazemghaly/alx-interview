#!/usr/bin/python3
'''interview taskes
'''


def isWinner(x, nums):
    ''' island prrimeter task interview
'''
    primes = []
    if x < 1 or not nums:
        return None
    if x != len(nums):
        return None
    marwin, benwin = 0, 0
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    for num in nums:
        primes_count = sum(primes[:num + 1]) 
        if primes_count % 2 == 1:
            marwin += 1
        else:
            benwin += 1
    if marwin == benwin:
        return None
    if marwin > benwin:
        return 'Maria'
    else:
        return 'Ben'
