# 기차 사이의 파리
import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1) :
    D, A, B, F = map(int, input().split())

    trains_s = [A, B]
    cnt = 0  # 파리의 이동 횟수
    d = D  # cnt 만큼 이동한 후 남은 거리
    Across_train = trains_s[1]  # 현재 파리와 반대로 움직이는 기차의 속도
    F_d = 0  # 파리의 이동 거리 -> (F * time)
    sum_fd = 0  # 정답...

    while d > 10**(-6) :
        time = d / (Across_train + F)   # t번째 이동 시간
        F_d = F * time  # 파리의 이동 거리
        d = d - ((A + B) * time)    # 이동 후 남은 거리
        Across_train = trains_s[cnt % 2]  # 파리와 반대편 기차 지정
        cnt += 1  # 파리의 이동 횟수

        sum_fd += F_d

    print(f'#{t} {sum_fd}')