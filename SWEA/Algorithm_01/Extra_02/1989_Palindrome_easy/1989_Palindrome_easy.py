# 1989 - 초심자의 회문 검사
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    word = input()
    result = 1

    if word != word[::-1]:
        result = 0

    print(f'#{t} {result}')