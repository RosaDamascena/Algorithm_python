# 15657 - N과 M(8)

'''
- N개의 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 고른 수열은 비내림차순이어야 한다.
    - 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
'''
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def N_M(depth, N, M):
    if depth == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, N + 1):
        answer.append(i)
        N_M(depth + 1, N, M)    # 재귀
        answer.pop()

N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = []

N_M(0, N, M)
