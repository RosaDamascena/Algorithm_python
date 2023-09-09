import sys
from itertools import combinations
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
num = sys.stdin.readline()
max_n = 0
c = list(combinations(num, N-K))

for i in c:
    if int(''.join(i)) > max_n:
        max_n = int(''.join(i))

print(max_n)