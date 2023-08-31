# 2178 - 미로 탐색
from collections import deque
import sys

sys.stdin = open('input.txt')


def BFS(r, c):
    queue = deque()
    queue.append((r, c))
    while queue:
        cur = queue.popleft()
        for i in range(4):
            x = cur[0] + dx[i]
            y = cur[1] + dy[i]
            if 0 <= x < N and 0 <= y < M:
                if maze[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    maze[x][y] = maze[cur[0]][cur[1]] + 1
                    queue.append((x, y))


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
BFS(0, 0)
print(maze[N - 1][M - 1])
