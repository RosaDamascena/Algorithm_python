# 2630 - 색종이 만들기
import sys
sys.stdin = open('input.txt')

def Divide(x, y, n):
    global white, blue
    color = confetti[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if confetti[i][j] != color:
                tmp = n // 2
                Divide(x, y, tmp)
                Divide(x + tmp, y, tmp)
                Divide(x, y + tmp, tmp)
                Divide(x + tmp, y + tmp, tmp)
                return

    if color == 0:
        white += 1
    else:
        blue += 1

N = int(sys.stdin.readline())
confetti = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
white = 0
blue = 0
Divide(0, 0, N)

print(white)
print(blue)
