# 15501 - 부당한 퍼즐
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
check_nums = list(map(int, input().split()))

idx = check_nums.index(nums[0])
check_1 = check_nums[idx:] + check_nums[:idx]
check_2 = check_nums[idx + 1:] + check_nums[:idx + 1]
check_2.reverse()

if nums == check_1 or nums == check_2:
    print('good puzzle')
else:
    print('bad puzzle')