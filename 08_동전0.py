import sys
input = sys.stdin.readline
N, K = map(int, input().split())

coins = []
for i in range(N):
    coins.append(int(input()))

total = 0
for coin in coins[::-1]:
    count = K//coin
    if count > 0:
        total += count
        K = K-(coin*count)
        if K == 0:
            break

print(total)