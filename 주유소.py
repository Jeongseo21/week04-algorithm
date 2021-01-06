import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

answer = []
idx = 0

while idx < n-1:
    tmp_dict = 0
    tmp = price[idx]
    while True:
        if price[idx] < tmp:
            answer.append(tmp * tmp_dict)
            print(answer)
            tmp = 0
        tmp_dict += dist[idx]
        idx += 1
