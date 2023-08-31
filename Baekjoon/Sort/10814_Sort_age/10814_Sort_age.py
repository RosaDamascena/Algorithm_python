# 10814 - 나이순 정렬
import sys
sys.stdin = open('input.txt')

N = int(input())
User = []
for _ in range(N):
    User.append(list(input().split()))

User.sort(key=lambda x : int(x[0]))

for i in range(N):
    print(User[i][0], User[i][1])
