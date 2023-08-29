# 11399 - ATM
import sys
sys.stdin = open('input.txt')

N = int(input())
Pi = list(map(int, input().split()))
Pi.sort()
sum_ls = 0
cnt = 0

for p in Pi:
    cnt += p
    sum_ls += cnt

print(sum_ls)