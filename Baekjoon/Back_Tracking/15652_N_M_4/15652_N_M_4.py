import sys
sys.stdin = open('input.txt')
'''
- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 고른 수열은 비내림차순이어야 한다.
'''

def N_M(node):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(node, N + 1):
        answer.append(i)
        N_M(i)    # 재귀
        answer.pop()

N, M = map(int, sys.stdin.readline().split())
answer = []

N_M(1)