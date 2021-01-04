import sys
input = sys.stdin.readline

n = int(input())
scores = [0]+[int(input()) for _ in range(n)]+[0]
dp = [0]*(n+10)
dp[1] = scores[1]
dp[2] = scores[1] + scores[2]

for i in range(3, n):
    dp[i] = max(dp[i-2]+scores[i], dp[i-3]+scores[i-1]+scores[i])
dp[n] = max(dp[n-2]+scores[n], dp[n-3]+scores[n-1]+scores[n])

print(dp[n])
