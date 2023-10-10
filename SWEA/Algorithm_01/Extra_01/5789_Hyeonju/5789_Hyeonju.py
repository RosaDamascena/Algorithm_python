import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1) :
    N, Q = map(int, input().split())    # N = 상자의 수, Q = 숫자를 변경할 횟수
    result = [0]*N # 상자에 적힌 숫자 값 리스트
    for i in range(1, Q+1) :
        L, R = map(int, input().split())  # L번 상자부터 R번 상자까지 i로 변경
        for j in range(L-1, R) :
            result[j] = i

    print(f'#{t}', *result)