import sys
sys.stdin = open('input.txt')

def DFS(cnt, list): # 순열 구하기
    print(list)
    if cnt == len(arr):
        perm_ls.append(list[:])
        return
    for j in arr:
        if visited[j] == 1:
            continue
        list.append(j)
        visited[j] = 1
        DFS(cnt+1, list)
        list.pop()
        visited[j] = 0

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    ground = [list(map(int, input().split())) for _ in range(N)]
    arr = [i for i in range(1, N)]
    visited = [0 for _ in range(N + 1)]
    perm_ls = []
    DFS(0, [])
    sum_ls = []

    for j in perm_ls:
        start, end = 0, 0
        tmp = 0
        for k in j:
            end = k
            tmp += ground[start][end]
            start = end
        tmp += ground[start][0]
        sum_ls.append(tmp)

    print('-------------------------------')
    print(perm_ls)
    print(sum_ls)
    print(f'#{t}', min(sum_ls))
    print('-------------------------------')