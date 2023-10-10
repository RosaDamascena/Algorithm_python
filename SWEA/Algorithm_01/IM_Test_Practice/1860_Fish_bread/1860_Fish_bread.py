# 1860 - 진기의 최고급 붕어빵
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split()) # M 분에 K개씩 만든다.
    men = sorted(list(map(int, input().split())))
    fish = 0    # 붕어빵 갯수
    cnt = 0     # 사람 수
    result = 'Possible'

    for i in range(0, men[-1]+1):   # i -> 초
        if i > 0 and i % M == 0 : # 붕어빵 추가
            fish += K
        while cnt < len(men) and men[cnt] == i:
            if fish > 0:
                fish -= 1
                cnt += 1
            else:
                result = 'Impossible'
                break

    print(f'#{t} {result}')