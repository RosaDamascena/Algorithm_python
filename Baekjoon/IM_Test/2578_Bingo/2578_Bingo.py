import sys
sys.stdin = open('input.txt')

def check():
    bingo = 0
    for x in Board:
        if x.count(0) == 5:
            bingo += 1

    for i in range(5):
        y = 0
        for j in range(5):
            if Board[j][i] == 0:
                y += 1
        if y == 5:
            bingo += 1

    d1 = 0
    for i in range(5):
        if Board[i][i] == 0:
            d1 += 1
    if d1 == 5:
        bingo += 1

    d2 = 0
    for i in range(5):
        if Board[i][4 - i] == 0:
            d2 += 1
    if d2 == 5:
        bingo += 1

    return bingo

Board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
numbers = []
for _ in range(5):
    numbers += list(map(int, sys.stdin.readline().split()))

cnt = 0
for k in range(25):
    a = numbers[k]
    for i in range(5):
        for j in range(5):
            if Board[i][j] == a:
                Board[i][j] = 0
                cnt += 1
    if cnt >= 12:
        result = check()

        if result >= 3:
            print(k+1)
            break
