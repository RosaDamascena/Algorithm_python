# 마법사 상어와 비바라기
import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
Board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
DS = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
Cloud = []
Cloud.append((N-1, 0))
Cloud.append((N-1, 1))
Cloud.append((N-2, 0))
Cloud.append((N-2, 1))

# 8개 방향 dict (r, c) 행 열
direction = {
    1: (0, -1),
    2: (-1, -1),
    3: (-1, 0),
    4: (-1, 1),
    5: (0, 1),
    6: (1, 1),
    7: (1, 0),
    8: (1, -1)
}

for i in range(M):
    # 1. d 방향 s만큼 이동
    d, s = DS[i]
    for j in Cloud:
        x, y = j
        nx, ny = x + direction[d][0], y + direction[d][1]
    # 2. 구름이 있는 칸 물 양 1 증가

    # 3. 물 복사 버그 시전
    # - 대각선 칸 물 여부 확인 cnt 증가
    # - r,c 에 있는 바구니의 물 cnt만큼 증가

    # 4. 전체 탐색 - 물의 양이 2 이상인 모든 칸에 구름 생성
    # - 물의 양 2 줄어든다.
    # - 원래 구름이 있던 칸이 아니여야 함( 구름 배열 만들기 )

    # 물의 양의 합 water 구하기
