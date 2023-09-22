# 11779 - 최소비용 구하기 2
import sys
sys.stdin = open('input.txt')
import heapq

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_n, next_w in graph[now]:
            if distance[next_n] > distance[now] + next_w:
                distance[next_n] = distance[now] + next_w
                parents[next_n] = now
                heapq.heappush(q, (distance[next_n], next_n))

    return distance[end]

INF = 1e9
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
parents = [0] * (N + 1)

for i in range(M):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append((e, w))

s_idx, e_idx = map(int, sys.stdin.readline().split())

print(dijkstra(s_idx, e_idx))

path = []
cur = e_idx
while cur:
    path.append(cur)
    cur = parents[cur]
print(len(path))
print(*path[::-1])