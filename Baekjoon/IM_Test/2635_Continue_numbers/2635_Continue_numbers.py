# 2635 - 수 이어가기
import sys
sys.stdin = open('input.txt')

def FindNum(first, second):
    result = first - second
    if result < 0:
        return []
    return [result] + FindNum(second, result)

N = int(sys.stdin.readline())

max_length = 0
result_numbers = []

for i in range(N+1):
    sequence = [N, i] + FindNum(N, i)
    if len(sequence) > max_length:
        max_length = len(sequence)
        result_numbers = sequence

print(len(result_numbers))
print(*result_numbers)
