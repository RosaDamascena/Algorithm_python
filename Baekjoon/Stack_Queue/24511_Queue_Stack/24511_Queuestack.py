# 24511 - queuestack
from collections import deque
import sys
sys.stdin = open('input.txt')

N = int(input())
Ai = list(map(int, input().split()))    # 0 = queue, 1 = stack
Bi = list(map(int, input().split()))   # 자료구조에 들어있는 원소
M = int(input())
C = list(map(int, input().split()))
queue = deque()
answer = []

for i in range(len(Ai)):
    if Ai[i] == 0:
        queue.appendleft(Bi[i])

for j in range(M):
    queue.append(C[j])
    answer.append(queue.popleft())

print(*answer)