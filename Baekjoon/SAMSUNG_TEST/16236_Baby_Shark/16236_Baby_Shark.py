# 16236 - 아기 상어
# 처음 아기 상어 크기 2
# 거리가 가까운 물고기가 많다면 가장 위에 있는 물고기 중 가장 왼쪽 부터
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

fish_size = {}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def BFS():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                deque.append((nx, ny))


N = int(input())
Space = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
result = 0
baby_shark = 2  # 초기 상태
queue = deque()

for i in range(N):
    for j in range(N):
        if Space[i][j] == 9:
            queue.append((i, j))
            Space[i][j] = 0

print(fish_size)

#BFS()