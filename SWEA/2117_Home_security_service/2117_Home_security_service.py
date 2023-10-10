# 2117 - 홈 방범 서비스
import sys
sys.stdin = open('input.txt')

T = int(input())
N, M = map(int, input().split())
Home = [list(map(int, input().split())) for _ in range(N)]
print(Home)
