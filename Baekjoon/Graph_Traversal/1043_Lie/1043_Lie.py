# 1043 - 거짓말
import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
truth = set(map(int, sys.stdin.readline().split()[1:]))
parties = [set(map(int, sys.stdin.readline().split()[1:])) for _ in range(M)]
possible = [1] * M

if not truth:
    print(M)
else:
    for _ in range(M):
        for i, party in enumerate(parties):
            if truth.intersection(party):
                truth.update(party)
                possible[i] = 0
    print(sum(possible))