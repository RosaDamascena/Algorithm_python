# 16236 - 아기 상어
# 처음 아기 상어 크기 2
# 거리가 가까운 물고기가 많다면 가장 위에 있는 물고기 중 가장 왼쪽 부터
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
Space = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
