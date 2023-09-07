import sys
from collections import deque
sys.stdin = open('input.txt')

def BFS(n):
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == K:
            print(visited[x])
            break
        dx = [-1, 1, x]
        for i in range(3):
            nx = x + dx[i]
            if 0 <= nx < (10 ** 5 + 2) and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)

def check_root(k):
    ds = [-1, 1, -s]
    pass

N, K = map(int, sys.stdin.readline().split())
visited = [-1] * (10 ** 5 + 1)
visited[N] = 0
BFS(N)
print(visited)
check_root(K)