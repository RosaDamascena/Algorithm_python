# 1259 - 패린드롬
import sys
sys.stdin = open('input.txt')

while True:
    A = list(map(int, input().rstrip()))
    if A[0] == 0:
        break
    else:
        if A == A[::-1]:
            print('yes')
        else:
            print('no')

