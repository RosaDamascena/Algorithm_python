# 1946 - 간단한 압축 풀기
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1) :
    N = int(input())
    c = 0
    print(f'#{t}')  # 테스트 케이스 번호 출력

    for n in range(N) :
        Ci, Ki = input().split()    # Ci = 알파벳, Ki = 1이상 20이하 정수
        Ki = int(Ki)
        for i in range(Ki) :
            if c < 10 :
                print(Ci, end='')
                c += 1
            elif c == 10 :
                print()
                print(Ci, end='')
                c = 1
    print()
