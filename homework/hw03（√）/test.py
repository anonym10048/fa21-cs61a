def ascending_coin(coin):
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(coins):
    def helper(n, m):
        if n == 0:
            return 1
        elif m > n or n < 0:
            return 0
        return helper(n - m, m) + helper(n, ascending_coin(m))
    return helper(coins, 1)


print(count_coins(20))