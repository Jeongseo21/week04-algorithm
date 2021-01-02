N = int(input())


def choose_num(i, checked):
    if i > schedule[-1][0]:
        return checked
    min_num = 2**31-1
    for leng in range(len(schedule)):
        if schedule[leng][0] >= i:
            min_num = min(schedule[leng][1], min_num)
    checked.append(min_num)
    return choose_num(min_num, checked)


schedule = []
for _ in range(N):
    start, end = map(int, input().split())
    schedule.append((start, end))

schedule.sort(key=lambda x: x[0])

checked = []
print(len(choose_num(0, checked)))

'''
12
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
4 4
'''