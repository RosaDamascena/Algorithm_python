# 5189 - 전자 카트
import sys
from itertools import permutations

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    ground = [list(map(int, input().split())) for _ in range(N)]
    arr = [i for i in range(1, N)]
    perm_ls = permutations(arr, N - 1)
    sum_ls = []

    for j in perm_ls:
        start, end = 0, 0
        tmp = 0
        for k in j:
            end = k
            tmp += ground[start][end]
            start = end
        tmp += ground[start][0]
        sum_ls.append(tmp)

    print(f'#{t}', min(sum_ls))
