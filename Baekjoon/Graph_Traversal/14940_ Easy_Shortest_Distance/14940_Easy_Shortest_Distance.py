# 14940 - 쉬운 최단거리
import sys
sys.stdin = open('input.txt')
from collections import deque


def BFS():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if land[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, sys.stdin.readline().split())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if land[i][j] == 2:
            visited[i][j] = 0
            queue.append((i, j))
        elif land[i][j] == 0:
            visited[i][j] = 0

BFS()

for k in visited:
    print(*k)
