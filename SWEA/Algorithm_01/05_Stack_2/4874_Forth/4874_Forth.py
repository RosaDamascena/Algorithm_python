# 4874 - Forth
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1) :
    Forth = list(input().split())
    stack = []
    result = 0

    for i in range(len(Forth)) :
        if Forth[i].isdigit() :
            stack.append(int(Forth[i]))
        elif Forth[i] == '.' :
            if len(stack) > 1 :
                print(f'#{t} error')
                break
            else :
                print(f'#{t}', *stack)
        else :
            if len(stack) >= 2 :
                if Forth[i] == '+':
                    b = stack.pop()
                    a = stack.pop()
                    result = a + b
                    stack.append(result)
                elif Forth[i] == '-' :
                    b = stack.pop()
                    a = stack.pop()
                    result = a - b
                    stack.append(result)
                elif Forth[i] == '*' :
                    b = stack.pop()
                    a = stack.pop()
                    result = a * b
                    stack.append(result)
                elif Forth[i] == '/' :
                    b = stack.pop()
                    a = stack.pop()
                    result = a // b
                    stack.append(result)
            else :
                print(f'#{t} error')
                break