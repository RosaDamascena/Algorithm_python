# 1242 - 암호코드 스캔
import sys

sys.stdin = open('input.txt')

code = {
    '0001101': '0', '0011001': '1', '0010011': '2',
    '0111101': '3', '0100011': '4', '0110001': '5',
    '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9',
}

ratio = {
    (2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4,
    (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9
}

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())  # N = 세로 크기, M은 가로 크기
    code_ls = list(set(input().strip('0') for _ in range(N)))
    code_ls = sorted(code_ls)[1:]
    answer = 0
    code_ans = []
    ls = []  # 암호 저장 리스트

    for c in code_ls:
        bin_code = bin(int(c, base=16))[2:] + '0'
        n1 = n2 = n3 = 0
        for i in bin_code:
            if i == '1' and n2 == 0 and n3 == 0:
                n1 += 1
            elif i == '0' and n1 != 0 and n3 == 0:
                n2 += 1
            elif i == '1' and n1 != 0 and n2 != 0:
                n3 += 1
            elif n1 > 0 and n2 > 0 and n3 > 0 and i == '0':
                r = min(n1, n2, n3)
                decode = ratio[n1 // r, n2 // r, n3 // r]
                ls.append(decode)
                n1 = n2 = n3 = 0

                if len(ls) == 8:
                    if ls not in code_ans:
                        code_ans.append(ls)
                        total = 0
                        for j in range(8):
                            if (j + 1) % 2 == 1:
                                total += ls[j] * 3
                            else:
                                total += ls[j]

                        if total % 10 == 0:
                            answer += sum(ls)
                    ls = []

    print(f'#{t} {answer}')
