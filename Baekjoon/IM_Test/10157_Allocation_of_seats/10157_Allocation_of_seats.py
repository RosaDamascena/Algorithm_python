# 10157 - 자리 배정
import sys
sys.stdin = open('input.txt')

R, C = map(int, input().split()) # 가로, 세로
K = int(input())
seats = [[0]*C for _ in range(R)]
r_ls = [0, 1, 0, -1]    # 행 리스트
c_ls = [1, 0, -1, 0]    # 열 리스트
answer = []
r, c = 0, 0
d = 0  # 방향 -> 우

for i in range(1, K+1) :
    seats[r][c] = i
    r += r_ls[d]
    c += c_ls[d]

    if r < 0 or c < 0 or r >= R or c >= C or seats[r][c] != 0 :
        r -= r_ls[d]    # 이전 상태로 돌리기
        c -= c_ls[d]
        d = (d + 1) % 4     # 방향 전환
        r += r_ls[d]    # 방향 전환 후 이동
        c += c_ls[d]

    if i == K:
        r -= r_ls[d]  # 이전 상태로 돌리기
        c -= c_ls[d]
        answer.append(r+1)
        answer.append(c+1)
        print(*answer)

    if K > (C * R):
        print(0)
        break