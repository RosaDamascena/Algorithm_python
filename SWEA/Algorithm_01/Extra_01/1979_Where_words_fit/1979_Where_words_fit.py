# 1979 - 어디에 단어가 들어갈 수 있을까
import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1) :
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    # 가로 확인
    for i in range(N) :
        cnt = 0
        for j in range(N) :
            if puzzle[i][j] == 1 :
                cnt += 1
            if puzzle[i][j] == 0 or j == N - 1 :
                if cnt == K :
                    result += 1
                if puzzle[i][j] == 0 :
                    cnt = 0

    # 세로 확인
    for i in range(N) :
        cnt = 0
        for j in range(N) :
            if puzzle[j][i] == 1 :
                cnt += 1
            if puzzle[j][i] == 0 or j == N - 1 :
                if cnt == K :
                    result += 1
                if puzzle[j][i] == 0 :
                    cnt = 0

    print(f'#{t}', result)