# 죽은 파리
import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1) :
    N, M = map(int, input().split())    # N = 판 크기, M = 파리채 크기
    board = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    D = [[0]*(N+1) for _ in range(N+1)] # 빈 합 배열 리스트
    sum_flies = []
    max_s = 0

    for i in range(1, N+1) :    # 합 배열
        for j in range(1, N+1) :
            D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + board[i][j]

    for k in range(1, N-M+2) :  # 원하는 구간의 합 배열
        r1, r2 = k, k+M-1
        for l in range(1, N-M+2):
            c1, c2 = l, l+M-1
            result = D[r2][c2] - D[r1-1][c2] - D[r2][c1-1] +D[r1-1][c1-1]
            sum_flies.append(result)
        
    for m in range(len(sum_flies)) :    # max 값
        if sum_flies[m] > max_s :
            max_s = sum_flies[m]

    print(f'#{t} {max_s}')

