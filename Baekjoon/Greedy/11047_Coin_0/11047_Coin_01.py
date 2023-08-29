# 11047 - 동전
import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
coin_val = [int(input()) for _ in range(N)]
answer = 0

for i in range(N-1, -1, -1):
    if coin_val[i] <= K:
        answer += K // coin_val[i]
        K = K % coin_val[i]

print(answer)