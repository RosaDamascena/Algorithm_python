# 숨바꼭질 3
import sys
from collections import deque
sys.stdin = open('input.txt')

def BFS(n):
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == K:
            print(visited[x])
            break
        dx = [-1, 1, x]
        for i in range(3):
            nx = x + dx[i]
            if 0 <= nx < ((10 ** 5) + 2) and not visited[nx]:
                    if i == 2:
                        visited[nx] = visited[x]
                        queue.appendleft(nx)
                    else:
                        visited[nx] = visited[x] + 1
                        queue.append(nx)


N, K = map(int, sys.stdin.readline().split())
visited = [0] * ((10 ** 5) + 2)
BFS(N)