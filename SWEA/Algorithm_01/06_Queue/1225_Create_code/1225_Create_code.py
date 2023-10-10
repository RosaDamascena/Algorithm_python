# 1225 - 암호 생성기
import sys
sys.stdin = open('input.txt')
from collections import deque

T = 10
for t in range(1, T+1) :
    tc = int(input())
    queue = deque(list(map(int, input().split())))  # 큐

    while True :
        for i in range(1, 6) :  # 한 사이클
            if (queue[0] - i) <= 0 :    # i 만큼 뺀 값이 0보다 작거나 같아질 때
                queue[0] = 0    # 0 으로 바꾸고
                queue.append(queue.popleft())   # 뒤로 보내준 후 브레이크
                break
            else :
                queue[0] -= i   # i 만큼 빼준 후
                queue.append(queue.popleft())   # 뒤로 보내기

        if queue[-1] == 0 : # while문 빠져나가기
            break

    print(f'#{t}', *queue)