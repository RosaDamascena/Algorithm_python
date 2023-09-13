# 1052 - 물병
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())

def check(n):
    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n //= 2
    return count

num = N
if K >= N:
    print(0)
else:
    while check(num) > K:
        num += 1
    print(num - N)
