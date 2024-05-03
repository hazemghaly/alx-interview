#!/usr/bin/python3
"""interview """


def makeChange(coins, total):
    '''
    making change in coins
    a pile of coins of different values
    determine the fewest number of
    coins needed to meet a given amount total
    '''
    n = len(coins)
    dp = [0] * (total + 1)
    dp[0] = 1
    if total <= 0:
        return 0
    for i in range(n):
        for j in range(coins[i], total + 1):
            dp[j] += dp[j - coins[i]]

    return dp[total] if dp[total] else -1
