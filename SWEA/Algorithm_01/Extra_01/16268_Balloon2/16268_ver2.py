# 16268 - 풍선2
import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())  # N = 행, M = 열
    balloon = [list(map(int, input().split())) for _ in range(N)]
    max_f = 0
    dr = [0, -1, 0, 1]  # 좌상우하
    dc = [-1, 0, 1, 0]

    # 각 풍선을 터뜨렸을 때 날릴 수 있는 꽃가루의 최대 개수 계산
    for i in range(N):  # 행
        for j in range(M):  # 열
            cnt = balloon[i][j] # 현재 위치의 폭탄 수로 초기화
            for d in range(4):  # 좌상우하
                r, c = i + dr[d], j + dc[d]
                if 0 <= r < N and 0 <= c < M:   # 범위 안에 있을 때만
                    cnt += balloon[r][c]
            if cnt > max_f:
                max_f = cnt

    print(f"#{t} {max_f}")
