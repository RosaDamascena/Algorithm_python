# 12851 - 숨바꼭질
import sys
from collections import deque
sys.stdin = open('input.txt')

def BFS(n):
    queue = deque()
    queue.append(n)
    while queue:
        global min_K, cnt_K
        x = queue.popleft()
        if x == K:
            cnt_K += 1
            continue
        dx = [-1, 1, x]
        for i in range(3):
            nx = x + dx[i]
            if 0 <= nx < ((10 ** 5) + 2):
                if not visited[nx] or visited[nx] == visited[x] + 1:
                    visited[nx] = visited[x] + 1
                    queue.append(nx)

N, K = map(int, sys.stdin.readline().split())
visited = [0] * ((10 ** 5) + 2)
cnt_K = 0
BFS(N)

print(visited[K])
print(cnt_K)