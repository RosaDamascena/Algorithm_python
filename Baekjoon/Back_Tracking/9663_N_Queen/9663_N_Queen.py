import sys
sys.stdin = open('input.txt')

def is_nqueen(x) :
    for i in range(x):
        if row[i] == row[x] or abs(row[x] - row[i]) == x - i:
            # 상하, 대각선 여부
            return False
    return True

def DFS(node) :
    global cnt
    if node == N :
        cnt += 1
        print(row)
    else :
        for j in range(1, N+1) :
            row[node] = j
            if is_nqueen(node) :
                DFS(node+1)
    return cnt

N = int(sys.stdin.readline())
cnt = 0
row = [0] * N
print(DFS(0))