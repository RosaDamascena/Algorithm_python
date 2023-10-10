import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0

    for i in range(N):
        for j in range(N):

            fly_stick = arr[i][j]
            for z in range(M):

                if i+z < N and j+z < N :
                    fly_stick += arr[i+z][j+z]

            max_num = max(max_num, fly_stick)

    print(f'#{tc} {max_num}')