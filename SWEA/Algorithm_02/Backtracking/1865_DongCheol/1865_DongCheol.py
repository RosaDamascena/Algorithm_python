# 1865 - DongCheol
import sys
sys.stdin = open('input.txt')

def Back(r, acc):
    global result
    if acc <= result:
        return

    if r == N:
        if acc > result:
            result = acc
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            Back(r + 1, acc * P[r][i])
            visited[i] = False


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    P = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 0
    Back(0, 100)
    print(f'#{t} {result:7f}')
