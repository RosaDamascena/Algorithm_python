# 1715 - 카드 정렬하기
import sys
sys.stdin = open('input.txt')
from queue import PriorityQueue

N = int(input())
pq = PriorityQueue()
for _ in range(N):
    pq.put(int(input()))

cards1 = 0
cards2 = 0
answer = 0

while pq.qsize() > 1:
    cards1 = pq.get()
    cards2 = pq.get()
    sum_c = cards1 + cards2
    answer += sum_c
    pq.put(sum_c)

print(answer)