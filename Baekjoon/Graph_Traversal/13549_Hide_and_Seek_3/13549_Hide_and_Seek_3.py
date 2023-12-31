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
        dx = [x, -1, 1]
        for i in range(3):
            nx = x + dx[i]
            if 0 <= nx <= (10 ** 5) and visited[nx] == -1:
                if i == 0:
                    visited[nx] = visited[x]
                else:
                    visited[nx] = visited[x] + 1
                queue.append(nx)


N, K = map(int, sys.stdin.readline().split())
visited = [-1] * (10 ** 5)
visited[N] = 0
BFS(N)
print(visited)