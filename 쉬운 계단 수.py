'''
-점화식-

dp[i][j] = 길이가 i이고 1의 자리가 j인 수

j = 0이면,    dp[i][j] = dp[i-1][j+1]
0 < j <9이면, dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
j =9이면,     dp[i][j] = dp[i-1][j-1]
'''
import sys
input = sys.stdin.readline

N = int(input())
dp = [[0]*10 for _ in range(N+1)]
dp[1][0] = 0
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif 0< j <9:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
# print(dp[N])
print(sum(dp[N])%1000000000)

