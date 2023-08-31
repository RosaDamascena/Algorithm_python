import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

que = deque()
N = int(input())
for i in range(N) :
    order = list(map(str, input().split()))
    if order[0] == 'push_front':
        que.appendleft(order[1])
    elif order[0] == 'push_back':
        que.append(order[1])
    elif order[0] == 'pop_front':
        if not que:
            print(-1)
        else:
            print(que.popleft())
    elif order[0] == 'pop_back':
        if not que :
            print(-1)
        else :
            print(que.pop())
    elif order[0] == 'size':
        print(len(que))
    elif order[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if que :
            print(que[0])
        else :
            print(-1)
    elif order[0] == 'back':
        if que :
            print(que[-1])
        else :
            print(-1)