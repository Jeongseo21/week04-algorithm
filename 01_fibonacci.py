
N = int(input())
fibo = [0]*(100)

fibo[1] = 1
fibo[2] = 1

for i in range(3, N+1):
    fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[N])
