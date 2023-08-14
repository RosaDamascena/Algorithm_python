# 15649 - N과 M(2)
'''
- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.
'''
import sys
sys.stdin = open('input.txt')

def N_M(depth, N, M):
    if depth == M:
        #print(' '.join(map(str, answer)))
        stack.append(sorted(answer))
        #print(stack)

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            answer.append(i)

            N_M(depth + 1, N, M)    # 재귀
            visited[i] = False
            answer.pop()

    return stack

N, M = map(int, input().split())
visited = [False] * (N + 1)
answer = []
stack = []
result = []


r1 = N_M(0, N, M)
for r in r1 :
    if r not in result:
        result.append(r)
        print(*r)

