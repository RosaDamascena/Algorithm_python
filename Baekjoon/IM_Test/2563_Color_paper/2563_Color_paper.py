# 2563 - 색종이
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
board = [[0] * 101 for _ in range(101)]
for n in range(N):
    x, y = map(int, sys.stdin.readline().split())

    for i in range(y, y+10):
        for j in range(x, x+10):
            board[i][j] = 1

cnt = 0
for k in board:
    cnt += k.count(1)

print(cnt)
