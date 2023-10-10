# 5185 - 이진수
import sys

sys.stdin = open('input.txt')

#hex_to_bin = {hex(i).replace('0x', '').upper() : f'{i:04b}' for i in range(16)}
#print(hex_to_bin)
hex_to_binary = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}

T = int(input())
for t in range(1, T + 1):
    N, hex_num = input().split()
    result = ''
    for char in hex_num:
        result += hex_to_binary[char]

    print(f'#{t} {result}')
