# 백트래킹

def solution(arr, end, result) :
    if result != 10 :
        return
    for i in range(1, end+1) :
        if arr[i] :
            print(data[i], end=' ')
    print()

def construct_candidates(c):
    c[0] = True
    c[1] = False
    return c

def backtracking(arr, now, end, result) :
    global cnt
    cnt += 1

    c = [0] * 2

    if now == end :
        solution(arr, end, result)
    else :
        now += 1
        ncandidates = construct_candidates(c)
        for i in range(len(ncandidates)) :
            arr[now] = c[i]
            if arr[now] :
                backtracking(arr, now, end, result + data[now])
            else:
                backtracking(arr, now, end, result)

NMAX = 12
cnt = 0
data = list(range(11))

arr = [0] * NMAX
backtracking(arr, 0, 10, 0)
print(cnt, 'cnt')