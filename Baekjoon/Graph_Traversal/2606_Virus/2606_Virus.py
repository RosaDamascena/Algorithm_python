# 2606 - 바이러스
import sys
sys.stdin = open('input.txt')

# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수 구하기
def DFS(node) :
    global cnt
    visited[node] = True        # 현재 노드를 방문 처리

    for next in CF[node] :      # 현재 노드와 연결된 노드들 확인
        if not visited[next] :  # 아직 방문하지 않은 노드라면
            DFS(next)           # 해당 노드로 DFS를 재귀 호출
            cnt += 1            # DFS가 종료할 때마다 감염된 컴퓨터 수 증가

    return cnt                  # DFS가 종료될 때마다 감염된 컴퓨터 수 반환

N = int(sys.stdin.readline())   # 컴퓨터 수
F = int(sys.stdin.readline())   # 연결되어 있는 컴퓨터 쌍의 수
CF = [[] for _ in range(N+1)]   # 컴퓨터의 쌍 리스트 생성
visited = [False] * (N+1)       # 방문 확인 리스트
cnt = 0                         # 감염된 컴퓨터 수를 저장하는 변수 초기화

# 연결되어 있는 컴퓨터 쌍을 입력받고, CF 리스트에 저장
for f in range(F) :
    v1, v2 = map(int, sys.stdin.readline().split())
    CF[v1].append(v2)
    CF[v2].append(v1)

print(DFS(1))