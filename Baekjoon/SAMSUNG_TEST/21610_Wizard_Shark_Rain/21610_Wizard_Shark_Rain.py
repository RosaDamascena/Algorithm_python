# 마법사 상어와 비바라기
import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
Board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    # 물의 양이 적힌 board
DS = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]   # d = 방향, s = 횟수
Cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

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

# 대각선 (sr, sc)
diagonal = [(-1, -1), (1, -1), (-1, 1), (1, 1)]

for d, s in DS:
    # 1. d 방향 s만큼 이동
    move_cloud = []
    for x, y in Cloud:
        nx, ny = (x + direction[d][0] * s) % N, (y + direction[d][1] * s) % N
        move_cloud.append((nx, ny))
        # 2. 구름이 있는 칸 물 양 1 증가
        Board[nx][ny] += 1
    Cloud = move_cloud

    # 3. 물 복사 버그 시전
    for r, c in Cloud:
        cnt = 0  # 물 복사 임시 저장
        for sr, sc in diagonal:
            dr, dc = r + sr, c + sc
            if 0 <= dr < N and 0 <= dc < N:
                if Board[dr][dc] > 0:
                    cnt += 1
        Board[r][c] += cnt

    # 4. 전체 탐색 - 물의 양이 2 이상인 모든 칸에 구름 생성
    new_cloud = []
    for i in range(N):
        for j in range(N):
            if (i, j) not in Cloud and Board[i][j] >= 2:
                Board[i][j] -= 2
                new_cloud.append((i, j))
    Cloud = new_cloud

# result = 물의 양의 합 water 구하기
result = 0
for i in range(N):
    for j in range(N):
        result += Board[i][j]

print(result)