# 4834 - 숫자 카드

import sys
sys.stdin = open('NumCard_input.txt')

T = int(sys.stdin.readline())

for i in range(T) :
    N = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().rstrip()))
    sum_n = [0] * 10
    max_n = 0
    max_idx = 0

    for n in num_list :
        sum_n[n] += 1

    for s in range(len(sum_n)) :
        if sum_n[s] > max_n :
            max_n = sum_n[s]
            max_idx = s
        elif sum_n[s] == max_n and s > max_idx :
            max_n = sum_n[s]
            max_idx = s

    print(f'#{i+1} {max_idx} {max_n}')