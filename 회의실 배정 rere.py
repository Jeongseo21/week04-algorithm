import sys
input = sys.stdin.readline

N = int(input())

schedule = []
for _ in range(N):
    start, end = map(int, input().split())
    schedule.append((start, end))

schedule.sort(key=lambda x: (x[1], x[0]))
checked = 0

temp_start, temp_end = 0, 0
for start, end in schedule:
    if start >= temp_end:
        temp_start, temp_end = start, end
        checked += 1
print(checked)