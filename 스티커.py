'''

의사코드

점화식 :
dp[0][i] = buff[0][i]+(dp[1][i-1], dp[1][i-2])
dp[1][i] = buff[1][i]+(dp[0][i-1], dp[0][i-2])

T = 테스트 횟수를 입력
for _ in range(T):
    N = 스티커의 열의 수
    buff = 2행 N열
    dp = 2행 N열
    for i in range(N):
        stk0, stk1 = map(int, input().split())
        buff[0][i] = stk0
        buff[1][i] = stk1

        # i가 0 혹은 1인 경우 dp에 buff 그대로 넣어주기
        if i == 0:
            dp[0][0] = buff[0][0]
            dp[1][0] = buff[1][0]
            continue
        elif i == 1:
            dp[0][1] = buff[1][0] + buff[0][1]
            dp[1][1] = buff[0][0] + buff[1][1]
            continue

        # i가 2 이상인 경우 점화식 넣어주기
        dp[0][i] = buff[0][i]+(dp[1][i-1], dp[1][i-2])
        dp[1][i] = buff[1][i]+(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][N-1], dp[1][N-1]))



'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    buff = []
    dp = [[0]*N for _ in range(2)]

    for i in range(2):
        buff.append(list(map(int, input().split())))
    dp[0][0] = buff[0][0]
    dp[1][0] = buff[1][0]
    dp[0][1] = buff[1][0] + buff[0][1]
    dp[1][1] = buff[0][0] + buff[1][1]

    for i in range(N):
        # i가 2 이상인 경우 점화식 넣어주기
        dp[0][i] = buff[0][i]+max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = buff[1][i]+max(dp[0][i-1], dp[0][i-2])

    print(max(dp[0][N-1], dp[1][N-1]))