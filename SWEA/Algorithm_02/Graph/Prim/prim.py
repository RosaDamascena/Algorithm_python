# prim (최소 신장 트리)
import sys
sys.stdin = open('input.txt')

def prim(start):
    visited = [0] * (V + 1)
    visited[start] = 1
    result = 0
    for _ in range(1, V):
        next = 0
        min_val = 1e9
        for i in range(V + 1):
            if visited[i] == 1:
                for j in range(V + 1):
                    # 한 번 방문 한 적 있었던 i의 인접 노드 j
                    # 인접 행렬을 진출 가능한 노드에 대해서만 가중치를 기록
                    if graph[i][j] > 0 and not visited[j] and min_val > graph[i][j]:
                        next = j
                        min_val = graph[i][j]
        result += min_val
        visited[next] = 1
    return result

V, E = map(int, input().split())
graph = [[0] * (V + 1) for _ in range(V + 1)]


for _ in range(E):
    S, E, W = map(int, input().split())
    graph[S][E] = W
    graph[E][S] = W

print(prim(0))