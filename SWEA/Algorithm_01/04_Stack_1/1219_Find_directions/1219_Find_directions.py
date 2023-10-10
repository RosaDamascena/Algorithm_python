# 1219 - 길찾기
import sys
sys.stdin = open('input.txt')

def DFS(node):   # 재귀 사용
    visited[node] = True    # 첫번째 노드를 방문하였으니 True로 바꾸어 준다.

    for next in range(1, 100):  # 0부터 시작하였기 때문에 next는 1부터 99까지 넣어준다.
        if matrix[node][next] == 1 and visited[next] == False:
            # 현재 노드의 next matrix값이 1이면서 방문을 안 했을 때
            if next == 99 : # next 값이 99라는 것은 시작 노드인 0부터 이어져 있다는 것이기 때문에 1을 반환한다.
                return True
            if DFS(next):   # 재귀함수 값이 True 일 때 1값 반환
                return 1

    return 0

for n in range(10):     # 테스트 케이스 10개
    t, E = map(int, input().split())    # t = 테스트 케이스 번호, E는 간선의 갯수
    data = list(map(int, input().split()))  # 입력 데이터
    matrix = [[0] * 100 for _ in range(100)]    # 간선 확인 데이터
    visited = [False] * 100     # 방문 여부

    for i in range(0, len(data), 2):    # 간선 입력
        matrix[data[i]][data[i + 1]] = 1    # 한 방향 순회

    print(f'#{t} {DFS(0)}')