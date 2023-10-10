# 2805 - 농작물 수확하기
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input().rstrip())) for _ in range(N)]
    answer = 0
    mid = N // 2
    start, end = mid, mid
    for i in range(N):
        for j in range(start, end+1):
            answer += farm[i][j]
        if i < mid:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1

    print(f'#{t} {answer}')