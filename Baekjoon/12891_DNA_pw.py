# 12891 - DNA password
import sys

S, P = map(int, sys.stdin.readline())   # S = 문자열 길이 / P = 부분문자열의 길이
A = list(sys.stdin.readline())  # 임의 문자열
alpha_list = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(0, S-P+1) :
    check_list = [0] * P
    for j in range(P):
        check_list.append(A[j])
        if A[j] in  :

        elif A[j] not in alpha_list :
            break