import timeit
COINS = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount: int) -> dict:
    coins = COINS
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count

    return result

# print(find_coins_greedy(113))
# print(find_coins_greedy(318))


def find_min_coins(amount: int) -> dict:
    coins = COINS
    dp = [float('inf')] * (amount + 1)
    prev = [-1] * (amount + 1)
    dp[0] = 0

    for i in range(amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev[i] = coin

    result = {}
    current = amount

    while current > 0:
        coin = prev[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result

        
# print(find_min_coins(113))
# print(find_min_coins(318))


print("Сума | Greedy (сек) | DP (сек)")
print("-" * 35)

amounts = [100, 1000, 5000, 10000]

for amount in amounts:
    greedy_time = timeit.timeit(
        lambda: find_coins_greedy(amount),
        number = 10
    )

    dp_time = timeit.timeit(
        lambda: find_min_coins(amount),
        number = 10
    )

    print(f"{amount:5} | {greedy_time:.6f} | {dp_time:.6f}")

