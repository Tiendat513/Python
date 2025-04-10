# Knapsack Problem
import sys
sys.stdin = open("Knapsack.inp", "r")
sys.stdout = open("Knapsack.out", "w")

# Read input
n, Wmax = map(int, input().strip().split())
weights = []
values = []

# Read weights and values
for _ in range(n):
    w, v = map(int, input().strip().split())
    weights.append(w)
    values.append(v)

def knapsack(n, Wmax, weights, values):
    # Initialize DP table
    dp = [[0] * (Wmax + 1) for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(Wmax + 1):
            # Option 1: Do not take the current item
            dp[i][w] = dp[i - 1][w]

            # Option 2: Take the current item (if it fits)
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])

    # The result is the maximum value for the full capacity
    return dp[n][Wmax]

# Solve the knapsack problem
result = knapsack(n, Wmax, weights, values)
print(result)