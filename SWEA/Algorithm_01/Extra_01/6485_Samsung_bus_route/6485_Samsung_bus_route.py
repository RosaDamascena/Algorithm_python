# 삼성 버스 노선
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1) :
    N = int(input())
    AB_list = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bus_route = [0]*5001
    result = []

    for j in AB_list :
        for k in range(j[0], j[1]+1) :   # 버스가 지나가는 수를 정류장마다 체크
            bus_route[k] += 1

    for i in range(1, P+1) :
        result.append(bus_route[int(input())])

    print(f'#{t}', *result)