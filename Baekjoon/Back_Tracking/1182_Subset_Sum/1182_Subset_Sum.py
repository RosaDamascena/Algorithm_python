# 1182 - 부분 수열의 합
import sys
sys.stdin = open('input.txt')

def Back(n):
    global cnt
    if sum(arr) == S and len(arr) > 0:
        cnt += 1
    for i in range(n, N):
        arr.append(N_ls[i])
        Back(i + 1)
        arr.pop()


N, S = map(int, sys.stdin.readline().split())
N_ls = list(map(int, sys.stdin.readline().split()))
cnt = 0
arr = []
Back(0)
print(cnt)