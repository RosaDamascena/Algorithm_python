# 14940 - 쉬운 최단거리
import sys
sys.stdin = open('input.txt')

n, m = map(int, sys.stdin.readline().split())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
