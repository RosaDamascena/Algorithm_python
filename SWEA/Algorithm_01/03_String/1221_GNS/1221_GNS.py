# GNS
import sys
sys.stdin = open('input.txt')

# 0~9까지의 숫자 리스트
number = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())    # 테스트 케이스 갯수
for t in range(1, T+1) :
    T_num, N = map(str, input().split())
    # 테스트 케이스 넘버 T_num과 숫자의 갯수 N을 입력 받는다.
    N = int(N)  # N을 정수형으로 바꿔준다.
    input_ls = list(map(str, input().split()))  # 숫자를 입력 받는다.
    cnt = [0]*10   # 각 숫자의 갯수를 세어줄 빈 리스트 생성

    for n in range(10) :    # input_ls를 순회하면서 각 숫자의 갯수를 세어준다.
        for i in range(N) :
            if input_ls[i] == number[n] :
                cnt[n] += 1


    print(f'#{t}')  # 테스트 넘버 출력

    for j in range(10) :
        # cnt 리스트의 숫자의 갯수를 확인하여 그 갯수만큼 number를 출력해준다.
        for k in range(cnt[j]) :
            print(number[j], end=' ')

    print()