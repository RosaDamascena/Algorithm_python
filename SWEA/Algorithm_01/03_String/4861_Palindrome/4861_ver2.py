import sys
sys.stdin = open('input.txt')

def solution(word, n):
    length = len(word)
    check = 0
    answer = []
    cnt = 0

    for k in range(length // 2) :
        if word[k] == word[length - 1 - k] :
            check += 1

    if check == (length // 2) :
        cnt += 1
        answer.append(word)
        print(f'#{n}', ''.join(*answer))

    return cnt

T = int(input())
for t in range(1, T+1) :
    N , M = map(int, input().split())
    str_ls = [list(map(str, input().rstrip())) for _ in range(N)]

    for i in range(N) :     # 가로, 세로 줄 탐색
        for j in range(N-M+1) :
            word_w = []
            word_h = []
            for wh in range(j, j+M) :
                word_w.append(str_ls[i][wh])
                word_h.append(str_ls[wh][i])

            cnt_w = solution(word_w, t)
            cnt_h = solution(word_h, t)

            if cnt_h == 1 or cnt_w == 1 :
                break

