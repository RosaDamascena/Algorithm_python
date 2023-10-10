# 풍선팡

import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1) :
    N, M = map(int, input().split())    # N = 행, M = 열
    balloon = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    max_f = 0
    dr = [0, -1, 0, 1] # 좌상우하
    dc = [-1, 0, 1, 0]
    flower = []

    for i in range(N) : # 행
        for j in range(M) : # 열
            cnt = balloon[i][j]
            for l in range(4):
                r = i
                c = j
                for k in range(balloon[i][j]) : # balloon[i][j] == 2
                    r += dr[l]  # i = 0
                    c += dc[l]  # j = -1
                    if r < 0 or c < 0 :
                        r -= dr[l]  # i = 0
                        c -= dc[l]
                        break
                    else :
                        try :
                            cnt += balloon[r][c]
                        except IndexError :
                            cnt += 0


            if cnt > max_f :
                max_f = cnt

    print(f'#{t} {max_f}')