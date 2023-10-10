import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1) :
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]   # 파리채를 칠 공간
    max_f = 0

    for i in range(N-M+1) :      # 파리채를 움직일 횟수만큼 반복
        for j in range(N-M+1) :
            fly = 0
            for k in range(M) :  # 파리채로 죽인 파리의 수 세기
                for l in range(M) :
                    fly += arr[i+k][j+l]

            if fly > max_f :
                max_f = fly

    print(f'#{t}', max_f)