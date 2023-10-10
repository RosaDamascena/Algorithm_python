# 회문2
import sys
sys.stdin = open('input.txt')

T = 10
for t in range(1, T + 1):
    N = int(input())
    ls = [list(input()) for _ in range(100)]
    ls_r = list(zip(*ls))
    max_l = 0

    for i in range(100):
        for cnt in range(100, 0, -1):   # cnt -> 문장의 길이
            if max_l >= cnt:    # max 값보다 길이가 짧은 문장은 확인할 필요 없음
                break
            for j in range(0, 100 - cnt + 1):
                word_r = ls[i][j : j + cnt]
                word_c = ls_r[i][j : j + cnt]
                if word_r == word_r[::-1]:  # 가로 체크
                    max_l = cnt
                    break
                if word_c == word_c[::-1]:  # 세로 체크
                    max_l = cnt
                    break

    print(f'#{t} {max_l}')
