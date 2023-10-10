# 1859 - 백만 장자 프로젝트
import sys
sys.stdin = open('input.txt')

def max_profit(prices):
    n = len(prices)
    max_profit = 0
    max_price = 0

    for i in range(n - 1, -1, -1):
        if prices[i] > max_price:  # 현재 날의 가격이 최대 가격보다 높다면 최대 가격을 업데이트
            max_price = prices[i]
        else:
            max_profit += max_price - prices[i]  # 최대 가격과 현재 날의 가격의 차이를 이익에 더함

    return max_profit

T = int(input())

for t in range(1, T + 1):
    N = int(input())  # 날짜 수
    prices = list(map(int, input().split()))  # 각 날짜의 매매가 리스트
    result = max_profit(prices)
    print(f"#{t} {result}")





