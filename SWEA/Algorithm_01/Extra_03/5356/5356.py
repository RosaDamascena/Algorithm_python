# 5356 - 의석이의 세로로 말해요
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    word_ls = [input() for _ in range(5)]

    print(f'#{t}', end=' ')
    for i in range(15):
        for j in range(5):
            try:
                print(word_ls[j][i], end='')
            except IndexError:
                continue
    print()