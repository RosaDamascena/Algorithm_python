# 5188 - 최소 합
import sys
import pprint
sys.stdin = open('input.txt')


def DP(x, y):
    if dp[x][y]:
        return dp[x][y]
    result = 3000
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            result = min(result, ls[x][y] + DP(nx, ny))
    dp[x][y] = result
    pprint.pprint(dp)
    return dp[x][y]


dx = [0, 1]  # 우, 하
dy = [1, 0]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    ls = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    dp[N - 1][N - 1] = ls[N - 1][N - 1]
    answer = DP(0, 0)

    print(dp)
    print(f'#{t} {answer}')
