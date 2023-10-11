# 포탑 부수기
import sys
sys.stdin = open('input.txt')

N, M, K = map(int, input().split())
Board = [list(map(int, input().split())) for _ in range(N)]
