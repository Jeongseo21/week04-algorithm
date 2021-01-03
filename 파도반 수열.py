'''
파도반 수열
점화식 : P(i) = P(i-1) + P(i-5)
'''
T = int(input())
cases = []
for _ in range(T):
    cases.append(int(input()))
P = [0]*101
P[1] = 1
P[2] = 1
P[3] = 1
P[4] = 2
P[5] = 2
for case in cases:
    for i in range(6, case+1):
        P[i] = P[i-5]+P[i-1]
    print(P[case])

