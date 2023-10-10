# 5105 - 미로의 거리
import sys
sys.stdin = open('input.txt')
from collections import deque

def BFS(x,y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 0
    while queue :
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if maze[nx][ny] == 0 :
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
                elif maze[nx][ny] == 3:
                    return visited[x][y]
    return 0

dx = [0,0,-1,1]
dy = [1,-1,0,0]

T = int(input())
for t in range(1, T+1) :
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[-1 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2 :
                print(f'#{t}', BFS(i, j))
                break
