# 2527 - 직사각형
import sys
sys.stdin = open('input.txt')

def check():
    pass

T = 4
for t in range(T):
    rectangles = list(map(int, input().split()))
    ax, ay, ap, aq, bx, by, bp, bq = map(int, rectangles)
    N = max(rectangles)

    print(draw)