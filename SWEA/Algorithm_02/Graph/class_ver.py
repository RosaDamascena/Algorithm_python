import sys
sys.stdin = open('input.txt')

def union(x, y):
    parent[x] = y
    #parent[y] = x

def find_set(x):
    parent[x]

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = list(range(N+1))
