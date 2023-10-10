# 1258 - 행렬 찾기
import sys
sys.stdin = open('input.txt')

def Search(ax, ay):
    i, j = ax, ay
    while i < n and Box[i][j]:  # 세로
        i += 1
    else:
        i -= 1
    while j < n and Box[i][j]:  # 가로
        j += 1
    else:
        j -= 1

    result.append([i - ax + 1, j - ay + 1])

    for k in range(ax, i+1):
        for l in range(ay, j+1):
            Box[k][l] = 0

    return result

T = int(input())
for t in range(1, T+1):
    n = int(input())
    Box = [list(map(int, input().split())) for _ in range(n)]
    result = []
    for x in range(n):
        for y in range(n):
            if Box[x][y]:
                Search(x, y)

    answer = sorted(result, key=lambda x: (x[0] * x[1], x[0]))

    print(f'#{t}', len(answer), end= ' ')
    for ans in answer:
        print(*ans, end=' ')
    print()
