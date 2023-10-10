# 3143 - 가장 빠른 문자열 타이핑
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1) :
    A, B = input().split()
    min_A = len(A)
    cnt = 0 # B 단어 철차 비교 갯수
    cnt_b = 0   # A안에 있는 B단어 갯수
    idx_a = 0   # A 인덱스
    idx_b = 0   # B 인덱스

    while idx_a < len(A) :  # A전체를 다 돌 때까지
        if A[idx_a] == B[idx_b] :   # A철자와 B철자가 일치할 때
            cnt += 1
            idx_a += 1
            idx_b += 1
            if cnt == len(B) :  # B가 완성될 때
                cnt_b += 1
                cnt = 0
                idx_b = 0
        elif cnt != 0 and A[idx_a] != B[idx_b] :    # 중간에 불일치할 때
            # 처음부터 확인해야 하기 때문에 A의 인덱스는 변경하지 않는다.
            cnt = 0 # 철자 갯수 초기화
            idx_b = 0   # B 인덱스 초기화

        elif cnt == 0 and  A[idx_a] != B[idx_b]:    # 처음부터 일치하지 않을 때
            idx_a += 1

    min_A = min_A - (cnt_b*len(B)) + cnt_b
    print(f'#{t}', min_A)