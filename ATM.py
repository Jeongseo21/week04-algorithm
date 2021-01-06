N = int(input())

time = list(map(int, input().split()))
time.sort()
tmp = 0
answer = []
for t in time:
    tmp += t
    answer.append(tmp)
print(sum(answer))