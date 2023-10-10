# 회문
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1) :
    N , M = map(int, input().split())
    str_ls = [list(map(str, input().rstrip())) for _ in range(N)]
    cnt = 0
    answer = []

    while cnt < 1 :
        for i in range(N) :     # 가로 줄 탐색
            for j in range(N-M+1) :
                word = str_ls[i][j:j+M]
                if word == word[::-1] :
                    cnt += 1
                    answer.append(word)

        if cnt == 1 :
            print(f'#{t}', ''.join(*answer))
            break

        for k in range(N) : # 세로 줄 탐색
            for l in range(N-M+1) :
                word_ls = []
                for w in range(l, l+M) :
                    word_ls.append(str_ls[w][k])
                if word_ls == word_ls[::-1] :
                    cnt += 1
                    answer.append(word_ls)

        if cnt == 1 :
            print(f'#{t}', ''.join(*answer))

