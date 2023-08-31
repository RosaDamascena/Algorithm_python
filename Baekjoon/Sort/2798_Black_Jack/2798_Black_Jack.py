# 2798 - 블랙잭
import sys
from itertools import combinations
sys.stdin = open('input.txt')

N, M = map(int, input().split())    # N : 카드 수, M : 부르는 카드
cards = list(map(int, input().split()))

com = list(combinations(cards, 3))
answer = 0
for c in com:
    if answer < sum(c) <= M:
        answer = sum(c)

print(answer)


