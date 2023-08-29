# 13305 - 주유소
import sys
sys.stdin = open('input.txt')

N = int(input())
road_length = list(map(int, input().split()))
gas_cost = list(map(int, input().split()))

result = 0
m = gas_cost[0]
for i in range(N-1):
    if gas_cost[i] < m:
        m = gas_cost[i]
    result += m * road_length[i]
print(result)
