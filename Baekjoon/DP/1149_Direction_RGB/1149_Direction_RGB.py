# 1149 - RGB 거리
import sys
sys.stdin = open('input.txt')

N = int(input())
Cost = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    Cost[i][0] = min(Cost[i-1][1], Cost[i-1][2]) + Cost[i][0]
    Cost[i][1] = min(Cost[i-1][2], Cost[i-1][0]) + Cost[i][1]
    Cost[i][2] = min(Cost[i-1][0], Cost[i-1][1]) + Cost[i][2]

print(min(Cost[N-1]))