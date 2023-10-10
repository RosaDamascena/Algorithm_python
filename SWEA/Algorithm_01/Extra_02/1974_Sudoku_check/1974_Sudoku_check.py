# 1974 - 스도쿠 검증
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    s = [list(map(int, input().split())) for _ in range(9)]
    s_h = list(zip(*s))

    for i in range(9):  # 가로, 세로 한 줄씩 비교
        result = 0
        if len(set(s[i])) != 9:
            break
        elif len(set(s_h[i])) != 9:
            break
        else:
            result = 1

    for i in range(9):
        for j in range(0, 9, 3):
            pass


    print(f'#{t} {result}')