# 20055 - 컨베이어 벨트 위의 로봇
import sys
sys.stdin = open('input.txt')
from collections import deque

def Turn_Belt():    # 한 칸 회전
    A.rotate(1)
    Robot.rotate(1)
    Robot[-1] = 0

def Move_Robot():   # 로봇 이동
    for i in range(N-2, -1, -1):
        # 이동하려는 칸의 로봇, 내구도 확인
        if Robot[i] and not Robot[i+1] and A[i+1] > 0:
            Robot[i] = 0
            Robot[i+1] = 1
            A[i+1] -= 1     # 이동 후 내구도 -1
    Robot[-1] = 0

def Raise_Robot():  # 로봇 올리기
    # 올릴 곳에 로봇 있는지 확인
    # 내구도 0인지 확인
    if not Robot[0] and A[0] > 0:
        Robot[0] = 1
        A[0] -= 1

N, K = map(int, input().split())
A  = deque(map(int, input().split()))
Robot = deque([0] * N)
result = 0  # 단계

while True:
    result += 1
    Turn_Belt()
    Move_Robot()
    Raise_Robot()

    if A.count(0) >= K:
        break

print(result)