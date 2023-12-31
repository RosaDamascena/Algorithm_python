import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1) :
    board = [[0] * 10 for _ in range(10)]    # 그림판 생성(10*10)
    N = int(input())    # 그림 입력 갯수
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 입력값 2차원 배열

    cnt = 0  # 겹치는 부분의 갯수 변수 선언

    for i in range(N) :
        for r in  range(arr[i][0], arr[i][2]+1) :  # 행
            for c in range(arr[i][1], arr[i][3]+1) :  # 열
                if board[r][c] == 1 : # 이미 그림판에 그림이 그려져 있는 경우
                    cnt += 1    # 겹쳐진 부분의 갯수를 세어준다.
                board[r][c] += 1 # 그림판에 그림이 그려진 부분에 1을 더해준다.

    print(f'#{t} {cnt}')
    # 주어진 정보에서 같은 색인 영역은 겹치지 않는다.
    # 결국 색상값은 필요가 없었다...