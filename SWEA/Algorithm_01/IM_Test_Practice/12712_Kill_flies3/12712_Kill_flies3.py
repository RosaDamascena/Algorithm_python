# 12712 - 파리퇴치3
import sys
sys.stdin = open('input.txt')

T = int(input())
N, M = map(int, input().split())
Board = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
