# 1092 - 배
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
cranes_ls = list(map(int, input().split()))
M = int(input())
box_ls = list(map(int, input().split()))

cranes_ls.sort(reverse=True)
box_ls.sort(reverse=True)
cnt = 0

while box_ls:
    if box_ls[0] > cranes_ls[0]:
        cnt = -1
        break
    for crane in cranes_ls:
        for box in box_ls:
            if box <= crane:
                box_ls.remove(box)
                break
    cnt += 1

print(cnt)