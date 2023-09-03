# 1764 - 듣보잡
import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
not_hear_see = {}

for nm in range(N+M):
    hs = sys.stdin.readline()
    if hs not in not_hear_see:
        not_hear_see[hs] = 1
    else:
        not_hear_see[hs] += 1

answer = []
for k, v in not_hear_see.items():
    if v >= 2:
        answer.append(k)

answer = sorted(list(answer))
print(len(answer))
print(''.join(answer), end = '')