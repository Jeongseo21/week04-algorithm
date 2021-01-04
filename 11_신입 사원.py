import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    N = int(input().rstrip())
    scores = [0 for _ in range(N+1)]

    for _ in range(0, N):
        i, j = map(int, input().split())
        scores[i] = j

    min = scores[1]
    answer = 1
    for i in range(2, N+1):
        if scores[i] < min:
            answer += 1
            min = scores[i]
    print(answer)