import sys
input = sys.stdin.readline

expression = list(input().strip().split('-'))

answer = 0

for i in range(len(expression)):
    if '+' in expression[i]:
        nums = expression[i].split('+')
        temp = 0
        for num in nums:
            temp += int(num)
        expression[i] = temp

for i in range(len(expression)):
    if i == 0:
        answer += int(expression[i])
    else:
        answer -= int(expression[i])

print(answer)

'''
다른 사람 풀이

s = input().split('-')
cnt = 0
for ch in s[0].split('+'):
    cnt += int(ch)
for ch in s[1:]:
    for c in ch.split('+'):
        cnt -= int(c)
print(cnt)
'''