import sys
sys.stdin = open('input.txt')

n = int(input())
time = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))

answer = end = 0
for s, e in time:
    if s >= end:
        answer += 1
        end = e
print(answer)