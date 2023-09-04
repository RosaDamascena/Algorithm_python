# 1697 - 숨바꼭질
import sys
from collections import deque
sys.stdin = open('input.txt')

def BFS(n):
    queue = deque()
    queue.append(n)
    while queue:
        pass

N = int(input())
K = int(input())
x = N
dx = [-1, 1, x]
visited = [0] * (10**5)
BFS(N)