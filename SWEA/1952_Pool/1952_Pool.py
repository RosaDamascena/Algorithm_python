# 1952 - [모의 SW 역량 테스트] 수영장
import sys

sys.stdin = open('input.txt')
# 1일 이용권, 1달 이용권, 3달 이용권, 1년 이용권
# 10 40 100 300
T = int(input())
for t in range(1, T+1):
    day, month_1, month_3, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    min_sum = [0] * 13
    answer = 0

    for i in range(1, 13):
        if plan[i] * day <= month_1:
            min_sum[i] = min_sum[i-1] + (plan[i] * day)
        elif plan[i] * day > month_1:
            min_sum[i] = min_sum[i-1] + month_1

        if i >= 3 and (min_sum[i] - min_sum[i-3]) > month_3:
            min_sum[i] = min_sum[i-3] + month_3

    answer = min(min_sum[12], year)
    print(f'#{t}', answer)