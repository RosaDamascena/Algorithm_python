# 5099 - Pizza
import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for t in range(1, T+1) :
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))    # 치즈 양
    cheese_ls = []                              # 피자 번호와 치즈의 양을 함께 저장할 리스트

    for pizza in enumerate(cheese, start=1) :
        cheese_ls.append(list(pizza))           # 피자의 번호와 치즈 양 함께 저장
    print(cheese_ls)

    queue = deque()
    for i in range(N) :                         # 화덕에 피자 넣기
        queue.append(cheese_ls[i])

    next = N                                    # 다음에 넣을 피자의 인덱스, N-1 번째는 이미 들어감
    while len(queue) != 1 :                     # 마지막 하나가 남을 때까지
        if queue[0][1]//2 == 0 :                # 치즈의 양이 0이 될 때
            queue.popleft()                     # 빼버리기
            if next < M :                       # next의 범위가 피자의 갯수가 넘지 않을 때
                queue.append(cheese_ls[next])   # 다음 피자를 넣는다
                next += 1                       # 다음 피자 인덱스 +1
        else :                                  # 치즈의 양이 0이 아닐 때
            queue[0][1] //= 2                   # 치즈의 양 반 나누기
            queue.append(queue.popleft())       # 뒤로 보내기

    print(f'#{t}', queue[0][0])                 # 마지막 남은 피자의 번호 출력



