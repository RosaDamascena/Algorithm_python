# 1074 - Z
import sys
sys.stdin = open('input.txt')

def solution(x, y, n):
    global cnt
    print(cnt)
    if x == r and y == c:
        print(cnt)
        exit(0)
    if n == 1:
        cnt += 1
        return
    if not (x <= r < x + n and y <= c < y + n):
        cnt += n * n
        return

    n //= 2
    solution(x, y, n)
    solution(x, y + n, n)
    solution(x + n, y, n)
    solution(x + n, y + n, n)


N, r, c = map(int, sys.stdin.readline().split())
cnt = 0
solution(0, 0, 2 ** N)