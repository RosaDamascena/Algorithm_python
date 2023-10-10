# 4869 - 종이 붙이기(재귀 호출)
import sys
sys.stdin = open('input.txt')

def solution(n) :
    # 수열 : a(n) = a(n-1) + 2a(n-2)
    # a1과 a2 구해주기
    if n == 1 :     # a(1)
        return 1
    elif n == 2 :   # a(2)
        return 3
    elif n >= 3 :   # a(n)
        return solution(n-1) + 2*solution(n-2)

T = int(input())
for t in range(1, T+1) :
    N = int(input())
    n = N // 10
    answer = solution(n)

    print(f'#{t} {answer}')