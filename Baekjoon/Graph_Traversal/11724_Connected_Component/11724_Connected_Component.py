# 11724 - 연결 요소의 개수
import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

def DFS(n):
    global cnt
    visited[n] += cnt   # 방문 순서 표시
    for next in matrix[n]:
        if not visited[next]:
            DFS(next)
            cnt += 1
    return visited

matrix = [[] * (N + 1) for i in range(N + 1)]
visited = [0] * (N + 1)
cnt = 0
for m in range(M):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a].append(b)
    matrix[b].append(a)

DFS(1)
print(visited)