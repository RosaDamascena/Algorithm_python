# 1744 - 수 묶기
import sys
sys.stdin = open('input.txt')

N = int(input())
num_ls = [int(input()) for _ in range(N)]
num_ls.sort()
answer = []

while num_ls:
    if len(num_ls) >= 2:
        if num_ls[-1] > 1 and num_ls[-2] > 1:   # 1보다 큰 양수
            data1 = num_ls.pop()
            data2 = num_ls.pop()
            tmp = data1 * data2
            answer.append(tmp)
        elif num_ls[-1] == 1:  # 1일 때
            answer.append(num_ls.pop())
        elif num_ls[-1] <= 0:    # 0과 음수
            data1 = num_ls.pop(0)
            data2 = num_ls.pop(0)
            tmp = data1 * data2
            answer.append(tmp)
        else:
            answer.append(num_ls.pop())

    else:   # 스택에 하나 남았을 경우
        answer.append(num_ls.pop())

print(sum(answer))