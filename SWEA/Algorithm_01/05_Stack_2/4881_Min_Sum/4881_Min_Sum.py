# 4881 - 배열 최소 합
import sys
sys.stdin = open('input.txt')

def Search(now, acc):
    global min_ls
    if acc > min_ls :
        return
    if now == N :
        if acc < min_ls :
            min_ls = acc
    else :
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                Search(now + 1, acc + A[now][i])
                visited[i] = False


T = int(input())
for t in range(1, T+1) :
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * (N + 1)
    min_ls = 10 * N
    Search(0, 0)

    print(f'#{t}', min_ls)