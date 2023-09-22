# 15686 - 치킨 배달
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def Distance(chick):
    global min_c
    result = 0
    for i in home:
        tmp = 1e9
        for j in chick:
            dist = abs(i[0] - j[0]) + abs(i[1] - j[1])
            if tmp > dist:
                tmp = dist
        result += tmp
    if min_c > result:
        min_c = result
    return min_c

def Combi(idx, arr):
    if len(arr) == M:
        Distance(arr)
        return

    for i in range(idx + 1, len(chicken)):
        if not visited[i]:
            visited[i] = 1
            Combi(i, arr + [chicken[i]])
            visited[i] = 0

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

home = []
chicken = []
min_c = 1e9


for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])
visited = [0] * len(chicken)
Combi(-1, [])
print(min_c)