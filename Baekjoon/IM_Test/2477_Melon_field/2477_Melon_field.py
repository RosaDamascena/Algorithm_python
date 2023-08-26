# 2477 참외밭
# 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
import sys
sys.stdin = open('input.txt')

directions = []
length = []
K = int(input())
for _ in range(6):
    d, l = map(int, sys.stdin.readline().split())
    directions.append(d)
    length.append(l)

box_len, small_len = [], []
for i in range(1, 5):   # 4방향
    if directions.count(i) == 1:
        box_len.append(length[directions.index(i)])
        small_len.append(length[(directions.index(i) + 3) % 6])

box_area = (box_len[0] * box_len[1]) - (small_len[0] * small_len[1])
print(K * box_area)