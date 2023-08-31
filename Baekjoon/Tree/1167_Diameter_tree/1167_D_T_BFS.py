import sys
sys.stdin = open('input.txt')
from collections import deque

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        cur = queue.popleft()
        for i in A[cur]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                dis[i[0]] = dis[cur] + i[1]


N = int(input())
A = [[] for _ in range(N + 1)]

for _ in range(N):
    data = list(map(int, input().split()))
    idx = 0
    S = data[idx]
    idx += 1
    while True:
        E = data[idx]
        if E == -1:
            break
        V = data[idx + 1]
        A[S].append((E, V))
        idx += 2

dis = [0] * (N + 1)
visited = [False] * (N + 1)
BFS(1)
max_a = 1

for j in range(2, N + 1):
    if dis[j] > dis[max_a] :
        max_a = j

dis = [0] * (N + 1)
visited = [False] * (N + 1)
BFS(max_a)
dis.sort()
print(dis[N])