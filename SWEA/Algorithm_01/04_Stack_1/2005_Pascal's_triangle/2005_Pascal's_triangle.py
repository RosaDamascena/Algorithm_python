# 2005 - 파스칼의 삼각형
import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    pascal = []     # 정답 리스트
    print(f'#{t}')  # 테스트 케이스 번호 출력

    for i in range(N) :     # N만큼 반복
        stack = []      # 빈 스택 생성
        for j in range(i+1):    # i번째 길이만큼 반복
            if j == 0 or j == i:    # 양 끝값은 1 넣어주기
                stack.append(1)
            else:
                stack.append(pascal[i-1][j-1]+pascal[i-1][j])
                # 윗 줄의 j-1 번 째와 j번째 숫자를 더해 스택에 넣어줌

        pascal.append(stack)
        print(*pascal[i])   # i 번째 줄에 정답 출력
