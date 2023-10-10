# Prefix_sum
import sys
sys.stdin = open('sample_input.txt')

T = int(sys.stdin.readline())

for t in range(T) :
    N, M = map(int, sys.stdin.readline().split())    # N = 정수의 갯수, M = 구간의 갯수

    prefix_sum = [] # 구간 합
    answer = 0
    max_p = 0   # max 값 초기화
    min_p = float('inf')  # min 값 초기화

    Ai = list(map(int, sys.stdin.readline().split()))
    for i in range(N-M+1) :   # 0부터 N-M까지
        temp = 0    # 임시 값
        for j in range(i, i + M) :
            temp += Ai[j]
        prefix_sum.append(temp)

    for k in prefix_sum :
        if k > max_p :
            max_p = k

        if k < min_p :
            min_p = k

    answer = max_p - min_p

    print(f'#{t+1} {answer}')