# 피보나치 함수 1003

T = int(input())

fibonacci = [0]*41
fibonacci[0] = (1, 0)
fibonacci[1] = (0, 1)


for _ in range(T):
    N = int(input())

    for i in range(2, N+1):
        fibonacci[i] = (fibonacci[i-1][0] + fibonacci[i-2][0], fibonacci[i-1][1]+fibonacci[i-2][1])
    print(*fibonacci[N])


