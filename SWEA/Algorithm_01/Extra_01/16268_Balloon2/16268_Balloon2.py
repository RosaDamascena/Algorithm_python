# 16268 - 풍선2
import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1) :
    N, M = map(int, input().split())    # N = 행, M = 열
    board =[[0 for i in range(M+2)] for j in range(N+2)]
    cnt = 0
    max_f = 0
    flower = []

    for n in range(1, N+1) :
        line = list(map(int, input().split()))
        for m in range(1, M+1) :
            board[n][m] += line[m-1]

    for i in range(1, N+1) :
        for j in range(1, M+1) :
            cnt = 0
            cnt += board[i][j] + board[i-1][j] + board[i+1][j] + board[i][j-1] +board[i][j+1]
            flower.append(cnt)

    for f in flower :
        if f > max_f :
            max_f = f

    print(f'#{t} {max_f}')