# 9019 - DSLR
import sys
from collections import deque
sys.stdin = open('input.txt')

def BFS():
    while queue:
        n, result = queue.popleft()

        if n == B:
            print(result)
            return

        D = (2 * n) % 10000
        if not visited[D]:
            visited[D] = 1
            queue.append((D, result + 'D'))

        S = (n - 1) % 10000
        if not visited[S]:
            visited[S] = 1
            queue.append((S, result + 'S'))

        L = ((n % 1000) * 10) + (n // 1000)
        if not visited[L]:
            visited[L] = 1
            queue.append((L, result + 'L'))

        R = ((n % 10) * 1000) + (n // 10)
        if not visited[R]:
            visited[R] = 1
            queue.append((R, result + 'R'))


T = int(sys.stdin.readline())
for t in range(T):
    A, B = map(int, sys.stdin.readline().split())
    visited = [0] * 10001
    queue = deque()
    queue.append((A, ''))
    BFS()