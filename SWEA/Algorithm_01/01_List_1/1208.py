import sys

sys.stdin = open('input_Flatten.txt')

T = 10
for t in range(1, T+1):
    cnt = int(input())
    boxes = list(map(int,input().split()))
    for c in range(cnt):
        boxes.sort()
        boxes[0] += 1
        boxes[-1] -= 1
    boxes.sort()
    print(f'#{t} {boxes[-1] - boxes[0]}')
