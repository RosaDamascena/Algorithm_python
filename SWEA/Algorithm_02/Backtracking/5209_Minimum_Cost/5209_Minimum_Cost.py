import sys
sys.stdin = open('input.txt')

# nPr : n == r
# r : 사용중인 원소의 개수
# acc : 현재 경우의수 까지 누적된 값
def permutaion(r, acc):
    global result
    if acc > result:
        return
    # 종료 시점
    if r == N:
        if acc < result:
            result = acc
        return
    else:
        # 모든 공장이 하나씩은 만들어야하니
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                # A 공장의 1번 제품 생산비용을 acc에 누적 해본다음
                permutaion(r+1, acc+arr[r][i])
                # A 공장이 1번 제품을 안쓰고, 2번 제품을 썼을때
                visited[i] = False

T = int(input())
for t in range(1, T+1):
    # 배열의 길이
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # arr[?][i] 사용 여부
    visited = [0] * N
    # 비교 대상군
    result = sum(sum(arr, []))
    permutaion(0, 0)
    print(f'#{t}', result)