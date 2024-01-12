 # 15649 - N과 M(1)
'''
- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
'''
import sys
sys.stdin = open('input.txt')

def N_M(depth, N, M):
    if depth == M:
        print(' '.join(map(str, answer)))

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            answer.append(i)

            N_M(depth + 1, N, M)    # 재귀
            visited[i] = False
            answer.pop()


N, M = map(int, input().split())
visited = [False] * (N + 1)
answer = []

N_M(0, N, M)
