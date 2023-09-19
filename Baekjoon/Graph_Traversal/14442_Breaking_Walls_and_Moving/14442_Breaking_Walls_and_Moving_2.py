import sys
from collections import deque
sys.stdin = open('input.txt')

def BFS():
    while queue:
        x, y, breaking = queue.popleft()

        if x == N - 1 and y == M - 1:
            print(visited[x][y][breaking])
            return

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M :
                if Map[nx][ny] == 1 and breaking + 1 <= K and visited[nx][ny][breaking + 1] == 0:
                    visited[nx][ny][breaking + 1] = visited[x][y][breaking] + 1
                    queue.append((nx, ny, breaking + 1))
                elif Map[nx][ny] == 0 and visited[nx][ny][breaking] == 0:
                    visited[nx][ny][breaking] = visited[x][y][breaking] + 1
                    queue.append((nx, ny, breaking))

    print(-1)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M, K= map(int, input().split())
Map = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0]*(K+1) for p in range(M)] for j in range(N)]
queue = deque()
queue.append((0, 0, 0))
visited[0][0][0] = 1
BFS()