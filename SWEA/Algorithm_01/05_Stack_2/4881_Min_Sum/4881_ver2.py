# 4881 - 배열 최소 합
import sys
sys.stdin = open('input.txt')

def DFS(depth, N):
    global sum_ls, min_ls
    if depth == N :
        for k in range(N):
            sum_ls += A[k][answer[k]]
        if sum_ls < min_ls :
            min_ls = sum_ls
        sum_ls = 0

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            answer.append(i)
            DFS(depth + 1, N)    # 재귀
            visited[i] = False
            answer.pop()
    return min_ls

T = int(input())
for t in range(1, T+1) :
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * (N + 1)
    sum_ls = 0
    min_ls = 10 * N
    answer = []

    print(f'#{t}', DFS(0, N))