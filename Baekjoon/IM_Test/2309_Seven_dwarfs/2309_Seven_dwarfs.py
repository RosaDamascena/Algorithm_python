# 2309 - 일곱 난쟁이
import sys
from itertools import combinations
sys.stdin = open('input.txt')

N = 9
N_list = [i+1 for i in range(N)]
combi = list(combinations(N_list, 7))

dwarfs = [0]
for i in range(N) :
    dwarfs.append(int(sys.stdin.readline()))

for j in range(len(combi)) :
    sum_height = 0
    height_d = []
    for k in combi[j] :
        sum_height += dwarfs[k]
        height_d.append(dwarfs[k])
    if sum_height == 100 :
        break

height_d.sort()
for n in range(7) :
    print(height_d[n])
