# 5201 - 컨테이너 운반
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    N_ls = list(map(int, input().split()))
    M_ls = list(map(int, input().split()))

    N_ls = list(reversed(sorted(N_ls)))
    M_ls = list(reversed(sorted(M_ls)))

    cnt = 0
    answer = 0
    for i in N_ls:
        if cnt == M:
            break
        if i <= M_ls[cnt]:
            answer += i
            cnt += 1
        else:
            continue

    print(f'#{t} {answer}')