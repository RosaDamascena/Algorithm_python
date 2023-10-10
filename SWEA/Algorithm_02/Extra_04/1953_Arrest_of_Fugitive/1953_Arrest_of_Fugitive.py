# 1953 - 탈주범 검거
import sys
from collections import deque
sys.stdin = open('input.txt')

Type = {
    1: [(-1, 0), (1, 0), (0, -1), (0, 1)],
    2: [(-1, 0), (1, 0)],
    3: [(0, -1), (0, 1)],
    4: [(-1, 0), (0, 1)],
    5: [(1, 0), (0, 1)],
    6: [(1, 0), (0, -1)],
    7: [(-1, 0), (0, -1)]
}

def BFS(r, c, cnt):
    global result
    queue  = deque()
    queue.append((r, c, cnt))
    visited[r][c] = 1

    while queue:
        x, y, cnt = queue.popleft()
        if cnt == L:
            return

        result += 1

        for dx, dy in Type[Tunnel[x][y]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and Tunnel[nx][ny] and not visited[nx][ny]:
                for sx, sy in Type[Tunnel[nx][ny]]:
                    if dx + sx == 0 and dy + sy == 0:
                        visited[nx][ny] = 1
                        queue.append((nx, ny, cnt+1))
                        break

T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    Tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    result = 0
    BFS(R, C, 0)
    print(f'#{t}', result)