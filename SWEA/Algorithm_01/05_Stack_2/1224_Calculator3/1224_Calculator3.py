# 1224 - Calculator3
import sys
sys.stdin = open('input.txt')

T = 10
for t in range(1, T+1):
    N = int(input())
    string = input()
    stack = []
    result = ''
    for i in string:
        if i.isdigit():  # 피연산자인지 아닌지 확인
            result += i
        else:
            if i == '(':
                stack.append(i)
            elif i == '*':
                while stack and stack[-1] == '*':
                    result += stack.pop()
                stack.append(i)
            elif i == '+':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
    while stack:
        result += stack.pop()

    stack = []
    for i in result:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(i))

    print(f'#{t}', stack.pop())