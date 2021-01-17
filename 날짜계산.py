E, S, M = map(int, input().split());

i = 1
while True:
    if i % 15 == E % 15 and i % 28 == S % 28 and i % 19 == M % 19:
        print(i)
        break
    i += 1
