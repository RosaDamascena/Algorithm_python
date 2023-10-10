# 4613 - 러시아 국기 같은 깃발
import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    min_f = N * M
    sum_a = 0
    for i in range(0, N - 2):  # white
        sum_a += M - flag[i].count('W')
        sum_b = 0
        for j in range(i + 1, N - 1):  # blue
            sum_b += M - flag[j].count('B')
            sum_c = 0
            for k in range(j + 1, N):  # red
                sum_c += M - flag[k].count('R')

            cnt = sum_a + sum_b + sum_c
            if cnt < min_f:
                min_f = cnt

    print(f'#{t} {min_f}')
