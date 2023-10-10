import sys

sys.stdin = open('input.txt')

V = int(input())
E = V - 1
edge = list(map(int, input().split()))
left = [0] * (V + 1)
right = [0] * (V + 1)
parent = [0] * (V + 1)

for i in range(E) :
    p, c = edge[i*2], edge[i*2+1]
    print(p, c)
    if left[p] == 0 :
        left[p] = c
    else :
        right[p] = c

print(left)
print(right)

