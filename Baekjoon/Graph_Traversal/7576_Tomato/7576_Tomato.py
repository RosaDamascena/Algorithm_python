# 7576 - 토마토
import sys
from collections import deque
sys.stdin = open('input.txt')

def BFS():
    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not Tomato[nx][ny]:
                Tomato[nx][ny] = Tomato[x][y] + 1
                queue.appendleft((nx, ny))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
M, N = map(int, sys.stdin.readline().split())
Tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0

queue = deque()
for i in range(N):
    for j in range(M):
        if Tomato[i][j] == 1:
            queue.appendleft((i, j))

BFS()
for k in Tomato:
    for l in k:
        if l == 0:
            print(-1)
            exit(0)

    answer = max(answer, max(k))
print(answer - 1)