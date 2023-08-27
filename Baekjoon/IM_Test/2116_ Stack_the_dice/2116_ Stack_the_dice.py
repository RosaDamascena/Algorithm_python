# 2116 - 주사위 쌓기
# A(0) - F(5), B(1) - D(3), C(2) - E(4)
import sys
sys.stdin = open('input.txt')

def checkMax(bottom, sum_d): # 주사위 옆면의 최댓값 구하기
    global answer
    cnt = 0
    while cnt != N: # cnt = 쌓은 주사위 갯수
        bottom_idx = Dices[cnt].index(bottom)
        top_idx = fair[bottom_idx]
        top = Dices[cnt][top_idx]
        dice = list(Dices[cnt])
        dice[bottom_idx] = 0
        dice[top_idx] = 0
        sum_d += max(dice)
        bottom = top
        cnt += 1

    answer = max(answer, sum_d)

fair = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}
N = int(sys.stdin.readline())
Dices = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0

for i in range(1, 7): # 맨 처음 주사위의 아랫면 값
    checkMax(i, 0)

print(answer)