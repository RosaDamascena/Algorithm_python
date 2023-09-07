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
            check_route(x)
            break
        dx = [-1, 1, x]
        for i in range(3):
            nx = x + dx[i]
            if 0 <= nx <= (10 ** 5) and not visited[nx]:
                visited[nx] = visited[x] + 1
                route[nx] = x
                queue.append(nx)

def check_route(x):
    answer = []
    n = visited[x]
    p = x
    for i in range(n + 1):
        answer.append(p)
        p = route[p]
    print(*answer[::-1])


N, K = map(int, sys.stdin.readline().split())
visited = [0] * (10 ** 5 + 1)
route = [0] * (10 ** 5 + 1)
BFS(N)