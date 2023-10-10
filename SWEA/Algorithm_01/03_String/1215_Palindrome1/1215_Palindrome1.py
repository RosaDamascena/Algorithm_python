# 회문 1
import sys
sys.stdin = open('input.txt')

def solution(word):     # 팰린드롬인지 확인하는 함수
    length = len(word)      # 단어의 길이
    check = 0       # 양 끝 값이 일치하는 횟수
    is_pal = False      # 회문 확인

    for k in range(length // 2):       # 홀수 일 때 가운데 확인X
        if word[k] == word[length - 1 - k]:
            check += 1

    if check == (length // 2):     # 회문일 때
        is_pal = True       # True 반환

    return is_pal

T = 10
for t in range(1, T+1):
    N = 8   # 8*8 크기의 글자판
    M = int(input())    # 찾아야 할 회문의 길이
    str_ls = [list(map(str, input().rstrip())) for _ in range(N)] # 입력값 리스트로 받아줌
    cnt = 0     # 회문 갯수 변수 선언
    # 가로, 세로 한번에 탐색
    for i in range(N):     # i는 탐색을 할 행 또는 열
        for j in range(N-M+1):  # N에서 M을 뺀 만큼만 이동
            word_w = []     # 가로 단어를 넣어줄 빈 리스트 선언
            word_h = []     # 세로 단어를 넣어줄 빈 리스트 선언

            for wh in range(j, j+M):    # M 길이만큼
                word_w.append(str_ls[i][wh])    # 가로
                word_h.append(str_ls[wh][i])    # 세로

            cnt += solution(word_w)     # 가로 회문 횟수 카운팅
            cnt += solution(word_h)     # 세로 회문 횟수 카운팅

    print(f'#{t}', cnt)


