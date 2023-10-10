# 9489 - 고대 유적
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    max_length = 0  # 가장 긴 구조물의 길이를 저장할 변수

    for i in range(N):
        cnt = 0
        for j in range(M):
            if A[i][j] == 1:
                cnt += 1
                if j == M - 1 and cnt > 1:
                    max_length = max(max_length, cnt)
            else:
                if cnt > 1:
                    max_length = max(max_length, cnt)
                cnt = 0

    for j in range(M):
        cnt = 0
        for i in range(N):
            if A[i][j] == 1:
                cnt += 1
                if i == N - 1 and cnt > 1:
                    max_length = max(max_length, cnt)
            else:
                if cnt > 1:
                    max_length = max(max_length, cnt)
                cnt = 0

    print(f'#{t}', max_length)
