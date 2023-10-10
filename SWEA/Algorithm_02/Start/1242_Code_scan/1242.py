import sys

sys.stdin = open('input.txt')

code = {
    '0001101': '0', '0011001': '1', '0010011': '2',
    '0111101': '3', '0100011': '4', '0110001': '5',
    '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9',
}

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())  # N = 세로 크기, M은 가로 크기
    code_ls = list(set(input().strip('0') for _ in range(N)))
    code_ls = sorted(code_ls)[1:]
    print(code_ls)
    answer = 0
    code_ans = []
    ls = []  # 암호 저장 리스트

    for c in code_ls:
        bin_code = bin(int(c, base=16))[2:].rstrip('0')
        l = (len(bin_code) // 56) + 1   # 배율
        bin_code = bin_code.zfill(56*(l))
        bin_code = bin_code[::l]
        print(bin_code)