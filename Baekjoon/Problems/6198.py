# 스택 - 옥상 정원 꾸미기

import sys

N = int(sys.stdin.readline())

building = []
cnt = 0
benchmarking = []

for i in range(N) :
    building.append(int(sys.stdin.readline()))

for j in range(N) :
    for k in range(j+1, N) :
        if (building[j] > building[k]) :
            cnt += 1
        else :
            break

        benchmarking.append(cnt)
        cnt = 0

print(sum(benchmarking))