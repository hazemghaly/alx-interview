#!/usr/bin/python3
"""interview """


def makeChange(coins, total):
    '''
    making change in coins
    a pile of coins of different values
    determine the fewest number of
    coins needed to meet a given amount total
    '''
    # n = len(coins)
    # dp = [0] * (total + 1)
    # dp[0] = 1
    # if total <= 0:
    #     return 0
    # for i in range(1, total + 1):
    #     for j in range(n):
    #         if coins[j] <= i:
    #             dp[i] += dp[i - coins[j]]
    # return dp[total] if dp[total] else -1
    n = len(coins)
    v = float('inf')
    dp = [v] * (total + 1)
    dp[0] = 0
    for i in range(1, total + 1):
        for j in range(n):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    return dp[total] if dp[total] != v else -1
