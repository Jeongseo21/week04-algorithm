import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    ranks = []
    for _ in range(N):
        rank1, rank2 = map(int, input().split())
        ranks.append([rank1, rank2, True])
    ranks.sort(key=lambda x:x[0])
    flag = True
    for i in range(N):
        if ranks[i][1] == 1:
            flag = False

            continue
        if not flag:
            ranks[i][2] = False

    ranks.sort(key=lambda x:x[1])
    flag = True
    for i in range(N):
        if ranks[i][0] == 1:
            flag = False
            continue
        if not flag:
            ranks[i][2] = False

    answer = 0
    for rank in ranks:
        if rank[2]:
            answer += 1
    print(answer)