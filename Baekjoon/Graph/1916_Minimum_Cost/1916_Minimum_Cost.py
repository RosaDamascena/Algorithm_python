# 1916 - 최소 비용 구하기
import sys
sys.stdin = open('input.txt')
import heapq

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if not visited[now]:
            visited[now] = True
            for i in graph[now]:
                if not visited[i[0]] and distance[i[0]] > distance[now] + i[1]:
                    distance[i[0]] = distance[now] + i[1]
                    heapq.heappush(q, (distance[i[0]], i[0]))

    return distance[end]

INF = 1e9
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
visited = [False] * (N + 1)

for i in range(M):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append((e, w))

s_idx, e_idx = map(int, sys.stdin.readline().split())

print(dijkstra(s_idx, e_idx))
