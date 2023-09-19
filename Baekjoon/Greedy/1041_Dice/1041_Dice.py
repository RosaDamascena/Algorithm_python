# 1041 - 주사위
import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
Dice = list(map(int, sys.stdin.readline().split()))

min_Dice = [min(Dice[0], Dice[5]), min(Dice[1], Dice[4]), min(Dice[2], Dice[3])]
min_Dice.sort()

if N == 1:
    print(sum(Dice) - max(Dice))
else:
    D1 = min_Dice[0] * ((((N - 2) ** 2) * 5) + ((N - 2) * 4))
    D2 = (min_Dice[0] + min_Dice[1]) * ((N - 2) * 8 + 4)
    D3 = sum(min_Dice) * 4
    print(D1 + D2 + D3)