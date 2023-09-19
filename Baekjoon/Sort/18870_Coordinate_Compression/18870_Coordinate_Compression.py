# 18870 - 좌표 압축
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))
sorted_x = list(sorted(set(X)))
dict = {sorted_x[i] : i for i in range(len(sorted_x))}

for j in X:
    print(dict[j], end=' ')