# 1244 - 스위치 켜고 끄기
import sys

sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
switch = [0] + list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())
for i in range(N):
    s, n = map(int, sys.stdin.readline().split())  # s -> 남학생 - 1, 여학생 - 2
    start = 1
    k = 1
    if s == 1:  # 남학생일 때
        while n * start <= T:
            switch[n * start] = abs(switch[n * start] - 1)
            start += 1
    elif s == 2:  # 여학생일 때
        switch[n] = abs(switch[n] - 1)
        while 1 <= n - k and n + k <= T and switch[n - k] == switch[n + k]:
            switch[n - k] = abs(switch[n - k] - 1)
            switch[n + k] = abs(switch[n + k] - 1)
            k += 1

for i in range(1, T+1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()
