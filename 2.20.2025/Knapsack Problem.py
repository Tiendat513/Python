# Knapsack Problem
def knapsack(Wmax, weight, value, n):
    dp = [[0 for x in range(Wmax + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, Wmax + 1):
            if weight[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(value[i-1] + dp[i-1][w - weight[i-1]], dp[i-1][w])

    return dp[n][Wmax]

# Ví dụ sử dụng:
val = [60, 100, 120]
wt = [10, 20, 30]
Wmax = 50
n = len(val)
print(knapsack(Wmax, wt, val, n)) # Output: 220