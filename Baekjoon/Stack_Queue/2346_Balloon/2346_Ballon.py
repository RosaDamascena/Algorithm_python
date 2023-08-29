# 2346 - 풍선 터뜨리기
from collections import deque
import sys
sys.stdin = open('input.txt')


N = int(input())
queue = deque(enumerate(list(map(int, input().split())), start = 1))
answer = []

while queue:
    idx, balloon = queue.popleft()
    answer.append(idx)
    if balloon > 0:
        queue.rotate(-(balloon - 1))
    else:
        queue.rotate(-balloon)

print(*answer)