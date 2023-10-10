# 문자열 비교
import sys
sys.stdin = open('input.txt')


T = int(input())
cnt = 0

for t in range(1, T+1) :
    N = str(input())
    M = str(input())
    cnt = M.count(N)

    print(f'#{t}', cnt)