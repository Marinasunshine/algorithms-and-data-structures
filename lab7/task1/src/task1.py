def min_coins(money, coins):
    min_coins = [float('inf')] * (money + 1)
    min_coins[0] = 0

    for i in range(1, money + 1):
        for coin in coins:
            if i >= coin:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[money] == float('inf'):
        return -1
    else:
        return min_coins[money]