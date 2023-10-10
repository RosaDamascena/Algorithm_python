# 5432 - 쇠막대기 자르기
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    s = input()
    stack = []
    cnt = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            if s[i-1] == ')':
                stack.pop()
                cnt += 1
            elif s[i-1] == '(':
                stack.pop()
                cnt += len(stack)

    print(f'#{t} {cnt}')