# 1931 - 회의실 배정
import sys
sys.stdin = open('input.txt')

N = int(input())
meetings = [[0] * 2 for _ in range(N)]

for i in range(N):
    S, E = map(int, input().split())
    meetings[i][0] = E
    meetings[i][1] = S

meetings.sort()

cnt = 0
end = -1

for j in range(N):
    if meetings[j][1] >= end:
        end = meetings[j][0]
        cnt += 1

print(cnt)