import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for q in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    for i in nums:
        nums = sorted(nums)
        max_num = nums[-1:-(M+1):-1]
        min_num = nums[0:M:1]

        for sum_max_num in max_num:
            sum_max_num += sum_max_num

        for sum_min_num in min_num:
            sum_min_num += sum_min_num

        result = sum_max_num - sum_min_num

    print(f'#{q+1} {result}')