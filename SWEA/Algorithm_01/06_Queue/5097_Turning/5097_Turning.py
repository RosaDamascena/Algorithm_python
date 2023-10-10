# 5097 - 회전
import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for t in range(1, T+1) :
    N , M = map(int, input().split())
    queue = deque(list(map(int, input().split())))

    for m in range(M) : # M 번만큼
        queue.append(queue.popleft())   # 맨 앞 값 맨 뒤로 보내주기

    print(f'#{t}', queue[0])