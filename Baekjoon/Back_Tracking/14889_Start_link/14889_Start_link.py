# 14889 - 스타트와 링크
import sys
sys.stdin = open('input.txt')

def DFS(depth, idx):
    global min_d
    if depth == N // 2:
        Start, Link = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    Start += S[i][j]
                elif not visited[i] and not visited[j]:
                    Link += S[i][j]

        min_d = min(min_d, abs(Start-Link))
        return

    for k in range(idx, N):
        if not visited[k]:
            visited[k] = 1
            DFS(depth + 1, k + 1)
            visited[k] = 0

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [0] * N
min_d = 1e9

DFS(0, 0)
print(min_d)

