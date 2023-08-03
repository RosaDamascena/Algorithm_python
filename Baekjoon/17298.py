# 오큰수  NGE(i)

import sys

N = int(sys.stdin.readline())
A_list = list(map(int, sys.stdin.readline().split()))

stack = []
answer = []

for A in A_list :
    while stack and A < stack[-1] :
        stack.pop
    stack.append(A)

    print(stack)

