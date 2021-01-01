import sys

N = int(input())
gains = list(map(int, input().split()))
memo = [0]*101
memo[1] = gains[0]
memo[2] = max(gains[0], gains[1])

for i in range(3, N+1):
    memo[i] = max(memo[i-1], gains[i-1] + memo[i-2])
print(memo[N])