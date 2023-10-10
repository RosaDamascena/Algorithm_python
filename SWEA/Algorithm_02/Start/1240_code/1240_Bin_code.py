import sys

sys.stdin = open('input.txt')

code = {
    '0001101': '0', '0011001': '1', '0010011': '2',
    '0111101': '3', '0100011': '4', '0110001': '5',
    '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9',
}

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    code_ls = [input() for _ in range(N)]
    k = 0
    sum_odd = 0 # 홀수
    sum_even = 0 #짝수
    answer = 0

    for check in code_ls:
        if '1' in check:
            for i in range(M-1, 1, -1):
                if check[i] == '1' and k == 0:
                    k = i
                    break

            start = k - 56 + 1
            for i in range(1, 9):
                result = check[start:start+7]
                start += 7
                if i % 2 == 1:  # 홀수 자리
                    sum_odd += int(code[result])
                else:   # 짝수 자리
                    sum_even += int(code[result])
            break

    if (sum_odd * 3 + sum_even) % 10 == 0:
        answer = sum_odd + sum_even

    print(f'#{t} {answer}')