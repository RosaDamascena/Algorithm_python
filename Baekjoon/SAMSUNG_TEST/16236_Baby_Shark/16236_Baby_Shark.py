# 16236 - 아기 상어
# 처음 아기 상어 크기 2
# 거리가 가까운 물고기가 많다면 가장 위에 있는 물고기 중 가장 왼쪽 부터
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

def BFS(r, c):
    queue = deque()
    queue.append((r, c, 0))
    min_f = 1e9
    fishes = []
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1

    while queue:
        x, y, dist = queue.popleft()
        if dist > min_f:
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and Space[nx][ny] <= shark_size:
                if 0 < Space[nx][ny] < shark_size:
                    fishes.append((nx, ny, dist+1))
                    min_f = dist
                queue.append((nx, ny, dist + 1))
                visited[nx][ny] = 1

    return sorted(fishes, key=lambda x : (x[2], x[0], x[1]))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())    # 공간 크기
Space = [list(map(int, input().split())) for _ in range(N)] # 공간의 상태
move = 0  # 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아 먹을 수 있는 시간
shark_size = 2  # 초기 상태
eat = 0 # 잡아먹은 상어의 개수
r, c = 0, 0

for i in range(N):
    for j in range(N):
        if Space[i][j] == 9:
            r, c = i, j # 아기 상어 위치
            Space[i][j] = 0
            break

while True:
    fish = BFS(r, c)
    if fish:
        fx, fy, step = fish[0]
        move += step
        eat += 1
        Space[fx][fy] = 0
        r, c = fx, fy

        if eat == shark_size:
            shark_size += 1
            eat = 0
    else:
        break

print(move)