# 1753 - 최단 경로 구하기
import sys
from queue import PriorityQueue
sys.stdin = open('input.txt')

def Dijksstra():
    while q.qsize() > 0:
        cur = q.get()
        node = cur[1]

        if not visited[node]:
            visited[node] = True
            for tmp in graph[node]:
                next = tmp[0]
                value = tmp[1]
                if dist[next] > dist[node] + value:
                    dist[next] = dist[node] + value
                    q.put((dist[next], next))


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
INF = 1e9
dist = [INF] * (V + 1)
visited = [False] * (V + 1)
graph = [[] for _ in range(V + 1)]
q = PriorityQueue()

for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

q.put((0, K))
dist[K] = 0
Dijksstra()

for j in range(1, V + 1):
    if dist[j] == INF:
        print('INF', end=' ')
    else:
        print(dist[j], end=' ')