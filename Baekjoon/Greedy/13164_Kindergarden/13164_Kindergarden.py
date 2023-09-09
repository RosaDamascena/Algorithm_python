# 13164 - 행복 유치원
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
height = list(map(int, input().split()))
arr = []
for i in range(1, N):
    arr.append(height[i] - height[i - 1])

arr.sort()
print(sum(arr[:N-K]))