# 9375 - 패션왕 신해빈
import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    wear_dict = {}
    for i in range(N):
        name, type_w = map(str, sys.stdin.readline().split())
        if type_w in wear_dict:
            wear_dict[type_w].append(name)
        else:
            wear_dict[type_w] = [name]

    cnt = 1
    for j in wear_dict:
        cnt *= (len(wear_dict[j]) + 1)

    print(cnt - 1)