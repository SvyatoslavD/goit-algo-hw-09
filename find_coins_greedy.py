
import timeit


def find_coins_greedy(target, coins):

    result = {}

    coins.sort(reverse=True)

    for coin in coins:
        if target >= coin:
            count = target // coin
            target -= coin * count
            result[coin] = count
            if target == 0:
                break

    return result


coins = [50, 25, 10, 5, 2, 1]

#result = find_coins_greedy(113, coins)
#print(result)

targets = [113, 5222, 10121]
for target in targets:
    time = timeit.timeit(f"find_coins_greedy(target, coins)",
                         number=10,
                         globals=globals())
    print(f"{target:10}: {time:.6f} seconds")

print()
