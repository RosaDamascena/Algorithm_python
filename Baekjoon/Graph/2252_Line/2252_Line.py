# 2252 - 줄세우기
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indgree = [0] * (N + 1)
queue = deque()

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indgree[B] += 1

for i in range(1, N+1):
    if indgree[i] == 0:
        queue.append(i)
        
while queue:
    now = queue.popleft()
    print(now, end=' ')
    for next in graph[now]:
        indgree[next] -= 1
        if not indgree[next]:
            queue.append(next)