# 11723 - 집합
import sys
sys.stdin = open('input.txt')

M = int(sys.stdin.readline())
bit = 0

for m in range(M):
    ord = sys.stdin.readline().split()
    num = 0
    order = ord[0]
    if len(ord) == 2:
        num = int(ord[1])

    if order == 'add':
        bit |= (1 << num)
    elif order == 'remove':
        bit &= ~(1 << num)
    elif order == 'check':
        if bit & (1 << num) != 0:
            print(1)
        else:
            print(0)
    elif order == 'toggle':
        bit ^= (1 << num)
    elif order == 'all':
        bit = (1 << 21) - 2
    elif order == 'empty':
        bit = 0

    print(bit)
    print((1 << 20) - 1, '20')