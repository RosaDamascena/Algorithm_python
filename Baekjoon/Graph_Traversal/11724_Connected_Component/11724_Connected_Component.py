# 11724 - 연결 요소의 개수
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

def DFS(n):
    visited[n] = True
    for next in matrix[n]:
        if not visited[next]:
            visited[next] = True
            DFS(next)
    return visited

matrix = [[] * (N + 1) for i in range(N + 1)]
visited = [0] * (N + 1)
cnt = 0
for m in range(M):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a].append(b)
    matrix[b].append(a)

for i in range(1, N + 1):
    if not visited[i]:
        DFS(i)
        cnt += 1

print(cnt)