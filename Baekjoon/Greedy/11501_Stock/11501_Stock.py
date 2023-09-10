# 11501 - 주식
import sys

sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    stock_prices = list(map(int, sys.stdin.readline().split()))
    profits = 0
    max_s = 0

    for i in range(N - 1, -1, -1):
        if stock_prices[i] > max_s:
            max_s = stock_prices[i]
        else:
            profits += max_s - stock_prices[i]

    print(profits)
