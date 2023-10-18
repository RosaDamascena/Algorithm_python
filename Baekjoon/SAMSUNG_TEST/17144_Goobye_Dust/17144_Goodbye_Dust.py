# 17144 - 미세먼지 안녕!
import sys
sys.stdin = open('input.txt')

def Diffusion_dust():
    px = [-1, 1, 0, 0]
    py = [0, 0, -1, 1]
    Add = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if A[i][j] != 0 and A[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx, ny = i + px[k], j + py[k]
                    if 0 <= nx < R and 0 <= ny < C and A[nx][ny] != -1:
                        Add[nx][ny] += A[i][j] // 5
                        tmp += A[i][j] // 5
                Add[i][j] -= tmp

    for i in range(R):
        for j in range(C):
            A[i][j] += Add[i][j]


def Cycle_air_up():
    # up 일 때
    ux = [0, -1, 0, 1]  # 우, 상, 좌, 하
    uy = [1, 0, -1, 0]
    x, y = up, 0
    u = 0   # 방향 전환
    tmp = 0
    while True:
        rx, ry = x + ux[u], y + uy[u]
        if rx == up and ry == 0:
            break
        if 0 <= rx < R and 0 <= ry < C:
            A[rx][ry], tmp = tmp, A[rx][ry]
            x, y = rx, ry
        else:
            u += 1

def Cycle_air_down():
    # down 일 때
    dx = [0, 1, 0, -1]  # 우, 하, 좌, 상
    dy = [1, 0, -1, 0]
    x, y = down, 0
    d = 0
    tmp = 0
    while True:
        rx, ry = x + dx[d], y + dy[d]
        if rx == down and ry == 0:
            break
        if 0 <= rx < R and 0 <= ry < C:
            A[rx][ry], tmp = tmp, A[rx][ry]
            x, y = rx, ry
        else:
            d += 1

R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
cnt = 0
up = -1
down = -1

for i in range(R):
    for j in range(C):
        if A[i][j] == -1:
            up = i
            down = i + 1
            break
    if up != -1:
        break

for j in range(T):
    Diffusion_dust()
    Cycle_air_up()
    Cycle_air_down()

result = 0
for i in range(R):
    for j in range(C):
        if A[i][j] != -1 and A[i][j] != 0:
            result += A[i][j]

print(result)


