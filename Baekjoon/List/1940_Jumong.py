# 1940 - 주몽
# 투 포인터 알고리즘을 활용하여 갑옷을 만들 수 있는 조합의 개수 계산
import sys

N = int(sys.stdin.readline())   # 재료의 개수
M = int(sys.stdin.readline())   # 갑옷을 만드는데 필요한 재료의 수

# N개의 재료들이 가진 고유한 번호들
T = list(map(int, sys.stdin.readline().split()))


cnt = 0                         # 갑옷을 만들 수 있는 조합의 개수 변수 초기화
start = 0                       # 시작 인덱스
end = N-1                       # 끝 인덱스

T.sort()    # 재료들을 오름차순으로 정렬

while start < end:
    current_sum = T[start] + T[end] # 현재 합을 계산
    if current_sum == M:            # 현재 합이 목표 합과 같다면
        cnt += 1                    # 갑옷 조합의 개수 증가
        start += 1                  # 시작 인덱스 +1
        end -= 1                    # 끝 인덱스 -1
    elif current_sum < M:           # 현재 합이 목표 합보다 작다면
        start += 1                  # 시작 인덱스 +1
    else:                           # 현재 합이 목표 합보다 크다면
        end -= 1                    # 끝 인덱스 -1

print(cnt)
