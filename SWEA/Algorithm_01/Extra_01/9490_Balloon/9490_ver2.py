# 풍선팡
import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())  # N = 행, M = 열
    balloon = [list(map(int, input().split())) for _ in range(N)]
    max_f = 0
    dr = [0, -1, 0, 1]  # 좌상우하
    dc = [-1, 0, 1, 0]

    for i in range(N):  # 행
        for j in range(M):  # 열
            cnt = balloon[i][j]  # 풍선 자기자신의 위치 갯수로 초기화
            for l in range(4):  # 좌상우하 반복
                r, c = i, j  # 행, 열 중앙으로 초기화
                for k in range(balloon[i][j]):  # 폭탄이 퍼지는 범위
                    r += dr[l]
                    c += dc[l]
                    if r < 0 or c < 0 or r >= N or c >= M:  # 범위를 벗어났을 때
                        break  # k 반복문 종료
                    cnt += balloon[r][c]
            if cnt > max_f:
                max_f = cnt

    print(f'#{t} {max_f}')
