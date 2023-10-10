# 1220 - Magnetic
import sys
sys.stdin = open('input.txt')
# 1번은 아래  로 가야함, 2번은 위로 가야함

T = 10
for t in range(1, T+1):
    M = int(input())
    NS = [list(map(int, input().split())) for _ in range(M)]
    NS_turn = list(zip(*NS))
    cnt = 0 # 교착 개수

    for i in range(M):  # 행
        check = 0
        for j in range(M):  # 열
            if NS_turn[i][j] == 1: # N극일 때 오른쪽으로 이동
                check += 1
            elif NS_turn[i][j] == 2:
                if check:
                    cnt += 1
                    check = 0

    print(f'#{t} {cnt}')