# 4875 - 미로
import sys
sys.stdin = open('input.txt')

def DFS(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if not maze[nx][ny]:
                visited[nx][ny] = True
                if DFS(nx, ny):
                    return True
            elif maze[nx][ny] == 3:
                return True
    return False

dx = [0,0,-1,1]
dy = [1,-1,0,0]

T = int(input())
for t in range(1, T+1) :
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2 :
                print(f'#{t}', int(DFS(i, j)))