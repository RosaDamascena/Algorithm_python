# 1003 - 피보나치 함수
import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    zero = 1
    one = 0
    for _ in range(N):
        zero, one = one, zero + one

    print(zero, one)