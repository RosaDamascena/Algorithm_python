# 1223 - 계산기 2
import sys
sys.stdin = open('input.txt')

T = 10
for t in range(1, T+1) :
    N = int(input())
    A = input()
    x = 0
    y = 0
    result = ''
    stack = []
    answer = []

    # 우선순위가 높은 순으로
    for char in A:
        if char in '+-*/':
            if char in '*/':
                while stack and stack[-1] in '*/':
                    result += stack.pop()
                stack.append(char)
            elif char in '+-':
                while stack:
                    result += stack.pop()
                stack.append(char)
        else:
            result += char

    while stack:
        result += stack.pop()

    for r in result:
        cal = 0
        if r.isdigit() :    # 피연산자일 때
            answer.append(r)
        elif r == '*' :  # * 연산자일 때
            b = int(answer.pop())
            a = int(answer.pop())
            cal = a * b

            answer.append(cal)
        elif r == '+':  # + 연산자일 때
            b = int(answer.pop())
            a = int(answer.pop())
            cal = a + b
            answer.append(cal)

    print(f'#{t}', *answer)
