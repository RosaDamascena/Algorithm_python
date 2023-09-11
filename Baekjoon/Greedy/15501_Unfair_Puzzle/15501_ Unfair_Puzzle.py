# 15501 - 부당한 퍼즐
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
check_nums = list(map(int, input().split()))
reverse_nums = list(reversed(check_nums))
answer = 'bad puzzle'

for i in range(N):
    if nums == check_nums or nums == reverse_nums:
        answer = 'good puzzle'
        break
    check_nums.append(check_nums.pop(0))
    reverse_nums.append(reverse_nums.pop(0))

print(answer)