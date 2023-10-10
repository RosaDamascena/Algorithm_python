# 4408 - 자기 방으로 돌아가기
import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    Room = [sorted(list(map(int, input().split()))) for _ in range(N)]
    check_idx = [0] * N
    answer = 0
    while False in check_idx:
        check = -1
        cnt = 0
        for i in range(N):
            if Room[i][0] == Room[i][1]:
                check_idx[i] = 1
            elif check == -1 and not check_idx[i]:
                check_idx[i] = 1
                check = i
                cnt += 1
            elif Room[i][0] > Room[check][1] + 1:
                check_idx[i] = 1
                check = i
                cnt += 1
        if cnt > 0:
            answer += 1

    print(f'#{t} {answer}')
