# 13458 - 시험 감독
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())    # 시험장 수
A = list(map(int, input().split()))    # 각 시험장의 응시자 수
B, C = map(int, input().split())    # 총감독관 B명 가능, 부감독관 C명 가능
cnt = N

for i in A:
    i -= B
    if i > 0:
        if i % C:
            cnt += (i // C) + 1
        else:
            cnt += (i // C)

print(cnt)