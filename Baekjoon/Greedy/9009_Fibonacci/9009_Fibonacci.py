# 9009 - 피보나치
import sys
sys.stdin = open('input.txt')

def Fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)

T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())

print(Fibo(16))