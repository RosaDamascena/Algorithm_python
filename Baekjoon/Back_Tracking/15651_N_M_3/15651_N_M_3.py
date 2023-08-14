# 15651 - N과 M(3)
import sys
sys.stdin = open('input.txt')
'''
- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
'''

def N_M(depth, N, M):
    if depth == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, N + 1):
        answer.append(i)
        N_M(depth + 1, N, M)    # 재귀
        answer.pop()


N, M = map(int, input().split())
answer = []

N_M(0, N, M)