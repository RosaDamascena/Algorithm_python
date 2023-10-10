import sys
sys.stdin = open('input.txt')
def run_check(arr):  # run 체크
    for k in range(8):
        if arr[k] and arr[k + 1] and arr[k + 2]:
            return True
    return False

t = int(input())
for tc in range(1, 1 + t):
    arr = list(map(int, input().split()))
    player = [[0 for _ in range(10)] for _ in range(2)]
    result = 0
    for i in range(12):
        p = i % 2       # 플레이어 선택
        player[p][arr[i]] += 1
        if player[p][arr[i]] == 3:  # triplet 체크
            result = p + 1
            break
        if i >= 5:      # 3개 이상 들어온 경우
            if run_check(player[p]):    # run 체크
                result = p + 1
                break
    print(f'#{tc} {result}')