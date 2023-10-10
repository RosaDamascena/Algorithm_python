import sys
sys.stdin = open('input.txt')
from collections import deque

def BFS(S, G) :
    global cnt
    queue = deque()
    queue.append(S)
    while queue :
        curr = queue.popleft()
        cnt += 1
        for j in graph[curr] :
            if not visited[j] :
                visited[j] = visited[curr] + 1
                queue.append(j)
            if curr == G:
                return visited[G]
    return 0

T = int(input())
for t in range(1, T+1) :
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for i in range(E) :
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    S, G = map(int, input().split())
    cnt = 0

    print(f'#{t}', BFS(S, G))
