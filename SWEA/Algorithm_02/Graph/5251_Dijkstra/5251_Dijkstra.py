# 최소 이동 거리
import sys
sys.stdin = open('input.txt')

def Dijkstra():
    dist = [E * 100] * (V + 1)
    visited = [0] * (V + 1)
    dist[0] = 0

    for _ in range(V):
        next = 0
        min_val = E * 100

        for i in range(V + 1):
            if not visited[i] and min_val > dist[i]:
                next = i
                min_val = dist[i]
        visited[next] = 1

        for j in range(V + 1):
            if not visited[j] and dist[j] > dist[next] + arr[next][j]:
                dist[j] = dist[next] + arr[next][j]

    return dist[V]

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[E * 100] * (V+1) for _ in range(V+1)]

    for i in range(E):
        S, E, W = map(int, input().split())
        arr[S][E] = W

    print(f'#{t}', Dijkstra())