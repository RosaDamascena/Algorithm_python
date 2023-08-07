import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
mydeque = deque()
num_list = list(map(int, input().split()))

for i in range(N) :
    # 나보다 큰 데이터 삭제
    while mydeque and mydeque[-1][0] > num_list[i] :
        mydeque.pop()
    mydeque.append((num_list[i], i))

    if mydeque[0][1] <= i - L :
        mydeque.popleft()

    print(mydeque[0][0], end=' ')
