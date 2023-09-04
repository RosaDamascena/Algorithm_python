import sys

sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
wine_ls = [int(sys.stdin.readline()) for _ in range(n)]
max_DP = 0
DP = [0] * n
if n <= 2:
    print(sum(wine_ls))
else:
    DP[0] = wine_ls[0]
    DP[1] = DP[0] + wine_ls[1]
    for i in range(2, n):  # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
        DP[i] = max(DP[i - 1], DP[i - 3] + wine_ls[i - 1] + wine_ls[i], DP[i - 2] + wine_ls[i])
        if DP[i] > max_DP:
            max_DP = DP[i]
    print(max_DP)
