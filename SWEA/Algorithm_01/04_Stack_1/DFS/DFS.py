# DFS 구현
import sys
sys.stdin = open('input.txt')

def DFS(node) :
    stack = [node]
    visited = [False] * (V + 1)

    while stack :
        start = stack.pop()
        if visited[start] == 0 :
            visited[start] = True
            print(start, end=' ')
            for next in range(0, V+1) :
                if matrix[start][next] == 1 and visited[next] == 0 :
                    stack.append(next)


V, E = map(int, input().split())
data = list(map(int, input().split()))
matrix = [[0]*(V+1) for _ in range(V+1)]

for i in range(0, E*2, 2) :
    # print(i, i+1, data[i], data[i+1])
    matrix[data[i]][data[i + 1]] = 1
    matrix[data[i + 1]][data[i]] = 1
    '''
    matrix[1][2] = 1
    matrix[2][1] = 1

    matrix[data[0]][data[1]] = 1
    matrix[data[1]][data[0]] = 1

    matrix[data[2]][data[3]] = 1
    matrix[data[3]][data[2]] = 1
    '''

print(V, E)
print(data)
from pprint import pprint

pprint(matrix)
DFS(1)