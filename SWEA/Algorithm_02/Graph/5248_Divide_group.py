# 5248 - 그룹 나누기
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    ls = list(map(int, input().split()))

    graph = [0] * (N + 1)
    for i in range(0, M * 2, 2):
        if graph[ls[i]] == 0:
            graph[ls[i]] = ls[i]
            graph[ls[i+1]] = graph[ls[i]]
        else:
            graph[ls[i]]

    print(graph)
    print(list(set(graph[1:])))
