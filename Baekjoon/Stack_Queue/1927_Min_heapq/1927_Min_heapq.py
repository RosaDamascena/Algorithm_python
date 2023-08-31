import sys
import heapq
sys.stdin = open('input.txt')

N = int(input())
heap = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)