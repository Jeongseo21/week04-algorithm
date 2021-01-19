# 직사각형으로 나누기

# case 1

N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input())))

for i in range(1, M-2):
    for j in range(i+1, M-1):
        area1 =
