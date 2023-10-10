# 1961 - 숫자 배열 회전
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    N_ls = [list(map(str, input().split())) for _ in range(N)]
    N_zip = list(zip(*N_ls))
    answer = []

    for i in range(N):
        ls_90 = []
        answer.append(list(reversed(N_zip[i])))
        answer.append(list(reversed(N_ls[N-i-1])))
        answer.append(list(N_zip[-i-1]))

    print(f'#{t}')
    for j in range(3*N):
        print(''.join(answer[j]), end=' ')
        if (j+1) % 3 == 0:
            print()
