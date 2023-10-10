# 1244 - 최대 상금
import sys
sys.stdin = open('input.txt')

def DFS(idx, cnt):
    global answer
    print(answer)
    if cnt == change:
        answer = max(int(''.join(data)), answer)
        return
    for cur in range(idx, length):
        for i in range(cur + 1, length):
            if data[cur] <= data[i]:
                print(data, '전')
                data[cur], data[i] = data[i], data[cur]
                print(data, '후')
                DFS(cur, cnt + 1)
                data[cur], data[i] = data[i], data[cur]

    if answer == 0 and cnt < change:
        tmp = (change - cnt) % 2
        if tmp == 1:    # 홀수일 때만 마지막 두자리 교환
            data[-1], data[-2] = data[-2], data[-1]
        DFS(idx, change)

T = int(input())
for t in range(1, 7):
    data, change = list(map(str, input().split()))
    data = list(data)
    change = int(change)
    length = len(data)
    answer = 0
    DFS(0, 0)
    print(f'#{t} {answer}')




