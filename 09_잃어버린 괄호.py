import sys
input = sys.stdin.readline

expression = list(input().strip())

count = expression.count('-')

if count == 1:
    for i in range(len(expression)):
        if expression[i] == '-':
            expression[]