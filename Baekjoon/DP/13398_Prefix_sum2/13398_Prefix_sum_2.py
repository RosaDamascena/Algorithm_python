# 13398 - 연속합 2
# N개의 정수로 이루어진 수열에서 연속된 몇 개의 수를 선택하여
# 구할 수 있는 합 중 가장 큰 합 구하기
# 수열에서 하나의 수를 제거할 수 있다.(선택)
# 하나의 수를 제거하기 위해 좌합, 우합을 구한다.
# i번 째 수 제거시 -> L(i-1) + R(i+1)
import sys
sys.stdin = open('input.txt')
N = int(input())
numbers = list(map(int, input().split()))

L = [0] * N
L[0] = numbers[0]
R = [0] * N
R[N - 1] = numbers[N - 1]
answer = L[0]
for i in range(1, N):   # 좌합, 우합 구하기
     L[i] = max(numbers[i], L[i-1] + numbers[i])
     R[N - i - 1] = max(numbers[N - i - 1], R[N - i] + numbers[N - i - 1])
     if L[i] > answer:  # 연속된 수들의 합 중 최대값 구하기
         answer = L[i]

for j in range(1, N - 1):   # 숫자 1개 삭제된 상태
    delete = L[j-1] + R[j + 1]
    if delete > answer:
        answer = delete

print(answer)