N, M = map(int, input().split())

arr = list(map(int, input().split()))
answer = 0

sum_A = [0] * (N+1)

for i in range(1, N+1):
    sum_A[i] = sum_A[i-1] + arr[i-1]

for i in range(len(arr)):
    for j in range(i, len(arr)+1):
        if sum_A[j] < M:
            pass
        elif sum_A[j] - sum_A[i] > M:
            break
        elif sum_A[j] - sum_A[i] == M:
            answer += 1
            break
print(answer)