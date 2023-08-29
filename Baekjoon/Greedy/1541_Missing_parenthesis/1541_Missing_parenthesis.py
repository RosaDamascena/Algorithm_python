# 1541 - 잃어버린 괄호
import sys
sys.stdin = open('input.txt')

formula = list(map(str, input().split('-')))
result = []

for f in formula:
    f_ls = f.split('+')
    a = 0
    for i in f_ls:
        a += int(i)
    result.append(a)

while len(result) > 1:
    result.insert(0, (result.pop(0) - result.pop(0)))

print(*result)