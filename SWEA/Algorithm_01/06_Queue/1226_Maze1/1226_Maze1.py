# 1226 - 미로1
import sys
sys.stdin = open('input.txt')
from collections import deque

def BFS(x,y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    while queue :
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] :
                if maze[nx][ny] == 0 :
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                elif maze[nx][ny] == 3:
                    return 1
    return 0

dx = [0,0,-1,1]
dy = [1,-1,0,0]

T = 10
for t in range(1, T+1) :
    tc = int(input())
    N = 16
    maze = [list(map(int, input().rstrip())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2 :
                print(f'#{t}', BFS(i, j))
                break