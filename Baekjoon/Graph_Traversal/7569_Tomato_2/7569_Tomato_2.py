# 7569 - 3 차원 토마토
import sys
from collections import deque
sys.stdin = open('input.txt')

def BFS():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                    if not Tomato_ls[nx][ny][nz] and not visited[nx][ny][nz]:
                        visited[nx][ny][nz] = 1
                        Tomato_ls[nx][ny][nz] = Tomato_ls[x][y][z] + 1
                        queue.append((nx, ny, nz))


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, sys.stdin.readline().split())
Tomato_ls = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
queue = deque()
answer = 0

for h in range(H):  # 높이
    for n in range(N):  # 세로
        for m in range(M):  # 가로
            if Tomato_ls[h][n][m] == 1:
                queue.append((h, n, m)) # 높이, 세로, 가로
                visited[h][n][m] = 1

BFS()

for a in Tomato_ls:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(b))
print(answer - 1)
