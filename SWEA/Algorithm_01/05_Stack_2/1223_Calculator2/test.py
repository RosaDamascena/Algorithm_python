import sys
sys.stdin = open('input.txt')

T = 11
for t in range(1, T+1) :
    N = int(input())
    A = input()
    stack = []
    back = []

    x = 0
    y = 0
    for a in A :
        if a.isdigit() :    # 피연산자일 때
            back.append(a)
            print(back)
            if stack :
                back.append(stack.pop())
                print(back)
        else :  # 연산자일 때
            if a == '+' :
                stack.append(a)
                print(stack)
            elif a == '*' :
                stack.append(a)
                print(stack)
            else :
                if stack and a == '*' and stack[-1] == '+' :
                    stack.append(a)
                    print(stack)

