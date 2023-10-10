# 4408 - 자기방으로 돌아가기
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    check_list = [0] * 201
    max_c = 0
    for _ in range(int(input())):
        start, end = map(int, input().split())
        if start > end:
            start, end = end, start

        start = (start + 1) // 2
        end = (end + 1) // 2

        for i in range(start, end + 1):
            check_list[i] += 1

        for c in check_list:
            if c > max_c:
                max_c = c

    print(f'#{t} {max_c}')