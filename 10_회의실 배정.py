N = int(input())

schedule = {}
for _ in range(N):
    start, end = map(int, input().split())
    if start in schedule.keys():
        schedule[start] = min(schedule[start], end)
        continue
    schedule[start] = end

# sorted(schedule, key= lambda x:schedule[x])

def choose_num(i, checked):
    if i > max(schedule.keys()):
        return checked
    num = 2**31-1
    for idx, val in schedule.items():
        if idx >= i:
            num = min(num, val)
    checked.append(num)
    return choose_num(num, checked)


checked = []
checked = choose_num(0, checked)
print(len(checked))






