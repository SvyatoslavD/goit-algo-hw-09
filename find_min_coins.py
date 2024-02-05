
import timeit


def find_min_coins(target, coins):

    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for i in range(1, target + 1):
        for coin in coins:
            if i - coin >= 0:
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1

    result = {}
    while target > 0:
        for coin in coins:
            if target - coin >= 0 and dp[target] == dp[target - coin] + 1:
                if coin in result:
                    result[coin] += 1
                else:
                    result[coin] = 1
                target -= coin
                break

    return result


coins = [50, 25, 10, 5, 2, 1]

#result = find_min_coins(113, coins)
#print(result)

targets = [113, 5222, 10121]
for target in targets:
    time = timeit.timeit(f"find_min_coins(target, coins)",
                             number=10,
                             globals=globals())
    print(f"{target:10}: {time:.6f} seconds")

print()
