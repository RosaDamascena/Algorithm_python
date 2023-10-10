import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T) :
    K, N, M = map(int, input().split())
    station_list = list(map(int, input().split()))
    station_list.append(N)

    location = 0
    cnt = 0
    i = 0

    while location < N :
        location += K
        if location < station_list[i] :
            print(f'#{t+1} 0')
            break
        elif location >= N :
            print(f'#{t + 1} {cnt}')
            break

        while location >= station_list[i] :
            i += 1
        cnt += 1

        location = station_list[i-1]

