import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    D, A, B, F = map(int, input().split())
    time = D / (A + B)
    print(f"#{i + 1} {F * time}")
