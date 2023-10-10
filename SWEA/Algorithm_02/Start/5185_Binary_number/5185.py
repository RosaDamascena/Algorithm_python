# 5185 - 이진수
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, hex_num = input().split()

    print(f'#{t}', end=' ')
    for i in hex_num:
        print(bin(int(i, base=16))[2:].zfill(4), end='')
    print()

            