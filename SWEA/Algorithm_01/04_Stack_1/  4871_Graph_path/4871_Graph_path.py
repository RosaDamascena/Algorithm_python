# 4871 - 그래프 경로
import sys
sys.stdin = open('input.txt')

def DFS(S, G):  # 인접 노드 순회 stack 사용
    stack = [S]     # 시작 노드 지정
    visited = [False] * (V + 1) # 방문자 확인

    while stack:    # 스택이 비어있지 않을 때
        start = stack.pop() # 시작 노드
        if visited[start] == False: # 방문을 하지 않았을 때
            visited[start] = True   # 방문하였다고 표시
            for next in range(1, V + 1):    # next  V 순회
                if graph[start][next] == 1 and visited[next] == 0:
                    # 현재 노드의 next의 graph 값이 1이면서 방문을 안 했을 때
                    if next == G:   # next가 G일 때 시작노드 S에서 G까지 탐색 완료
                        return 1
                    stack.append(next)  # 아닐 때 next 값을 stack에 넣어준다.
    return 0

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())    # V = 노드 수, E = 간선 수
    visited = [0 for _ in range(V + 1)]     # 방문 표시
    graph = [[0 for _ in range(V + 1)] for _ in range(V + 1)]   # 그래프 간선 입력 리스트

    for _ in range(E):  # 간선 수 만큼
        i, j = map(int, input().split())    # 노드와 연결된 노드 입력 받기
        graph[i][j] = 1     # 간선 표시해주기

    S, G = map(int, input().split())    # 시작과 끝 값 입력 받기

    print(f'#{t} {DFS(S, G)}')  # S에서 G로 가는 경로가 존재하는지 확인하기