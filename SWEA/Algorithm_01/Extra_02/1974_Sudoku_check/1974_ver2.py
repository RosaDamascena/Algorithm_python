# 1974 - 스도쿠 검증
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    s = [list(map(int, input().split())) for _ in range(9)]
    s_h = list(zip(*s))

    result = 1  # 기본적으로 결과를 1로 설정 (맞으면 1, 아니면 0)

    for i in range(9):
        if len(set(s[i])) != 9 or len(set(s_h[i])) != 9:  # 가로와 세로 각각에 대해서 중복 검사
            result = 0
            break

    for i in range(0, 9, 3):  # 3 x 3 격자에 대한 검사
        for j in range(0, 9, 3):
            subgrid = [s[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if len(set(subgrid)) != 9:  # 3 x 3 격자 내에서 중복 검사
                result = 0
                break

    print(f'#{t} {result}')
