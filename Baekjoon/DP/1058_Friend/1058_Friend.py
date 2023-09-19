# 1058 - 친구
import sys
sys.stdin = open('input.txt')

def Famous_friend(n):
    two_friend = [[0] * n for _ in range(n)]
    for k in range(n):
        for l in range(n):
            for r in range(n):
                if l == r:
                    continue
                if Friendship[l][r] == 'Y' or (Friendship[l][k] == 'Y' and Friendship[k][r] == 'Y'):
                    two_friend[l][r] = 1

    max_f = 0
    for f in two_friend:
        max_f = max(max_f, sum(f))
    return max_f

N = int(sys.stdin.readline())
Friendship = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
result = Famous_friend(N)
print(result)