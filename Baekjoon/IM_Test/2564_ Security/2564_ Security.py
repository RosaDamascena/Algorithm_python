# 2564 - Security
# 1은 블록의 북쪽, 2는 블록의 남쪽, 3은 블록의 서쪽, 4는 블록의 동쪽
import sys
sys.stdin = open('input.txt')

def Find_d(dir, dist):
    if dir == 1:      # 북쪽
        return dist
    elif dir == 2:    # 남쪽
        return w + h + (w-dist)
    elif dir == 3:    # 서쪽
        return (2 * w) + h + (h-dist)
    else:                   # 동쪽
        return w + dist

w, h = map(int, sys.stdin.readline().split())   # 블록의 가로, 세로
length = (w + h) * 2 # 블록의 전체 둘레
N = int(sys.stdin.readline())   # 상점의 갯수
store_len = []
answer = 0
for n in range(N):  # 상점의 위치 방향, 좌표
    direction, distance = map(int, sys.stdin.readline().split())
    store_len.append(Find_d(direction, distance))

a, b = map(int, sys.stdin.readline().split())
security = Find_d(a, b)

for i in store_len:
    if abs(security - i) > (length // 2):
        answer += length - abs(security - i)
    else:
        answer += abs(security - i)

print(answer)