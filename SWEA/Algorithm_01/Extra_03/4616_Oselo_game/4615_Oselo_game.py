# 4615 - 재미있는 오셀로 게임
import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    B, W = 1, 2
    start = N // 2
    board = [[0] * N for _ in range(N)]
    board[start - 1][start - 1] = W
    board[start - 1][start] = B
    board[start][start - 1] = B
    board[start][start] = W
    check = []
    cnt_B = 0  # 흑돌의 갯수
    cnt_W = 0  # 백돌의 갯수
    dy = [-1, 1, 0, 0, -1, 1, -1, 1]  # 상하좌우 대각선
    dx = [0, 0, -1, 1, -1, 1, 1, -1]

    for i in range(M):
        x, y, color = map(int, input().split())
        board[y - 1][x - 1] = color
        for j in range(8):
            nx, ny = x - 1 + dx[j], y - 1 + dy[j]
            while 0 <= nx < N and 0 <= ny < N and board[ny][nx] != 0 and board[ny][nx] != color:
                check.append([nx, ny])
                nx, ny = nx + dx[j], ny + dy[j]
            if 0 <= nx < N and 0 <= ny < N and board[ny][nx] != color:
                check = []
            elif 0 <= nx < N and 0 <= ny < N and check and board[ny][nx] == color:
                for x1, y1 in check:
                    board[y1][x1] = color
            check = []

    for k in range(N):
        for l in range(N):
            if board[k][l] == B:
                cnt_B += 1
            elif board[k][l] == W:
                cnt_W += 1

    print(f'#{t} {cnt_B} {cnt_W}')
