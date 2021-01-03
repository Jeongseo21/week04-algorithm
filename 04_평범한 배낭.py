import numpy as np

N, K = map(int, input().split())

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    weight, value = map(int, input().split())
    for j in range(K+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-weight]+value, dp[i-1][j])

print(dp[-1][-1])